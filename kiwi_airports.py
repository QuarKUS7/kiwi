#!/usr/bin/python
# -*- coding: utf-8 -*-
# Autor: Peter Pagac

import requests
import argparse


def get_data(url):
    """call api and return json response"""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("[!] HTTP {0} calling [{1}]".format(response.status_code, url))
        return None

def process_data(data, args):
    """function for processing data to fit arg options"""
    if data:
        # no arguments option
        if not any(args.values()):
            # goal is to print out into stdout
            print({i: {'name': item['name'], 'IATA': item['id']}
                    for i, item in enumerate(data['locations'])})
            return None

        out = {i: { 'name': item['name'],
                    'IATA': item['id'],
                    'coords': item['location'],
                    'city': item['city']['name']}
                    for i, item in enumerate(data['locations'])}

        # full argument returns everything
        if args['full']:
            print(out)
            return None

        # drop not desired item in output dict
        for i, _ in out.items():
            if not args['iata']:
                del out[i]['IATA']
            if not args['coords']:
                del out[i]['coords']
            if not args['cities']:
                del out[i]['city']
            if not args['names']:
                del out[i]['name']
        print(out)
    else:
        print("No Airports Found")

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Get airports in the United Kingdom and display them on standard output.')
    parser.add_argument(
        "--names",
        action='store_true',
        help="to provide a name of the airport")
    parser.add_argument(
        "--cities",
        action='store_true',
        help="to provide a city with the airport")
    parser.add_argument(
        "--coords",
        action='store_true',
        help="to provide a coordinates of the airport")
    parser.add_argument(
        "--iata",
        action='store_true',
        help="to provide the IATA code of the airport")
    parser.add_argument(
        "--full",
        action='store_true',
        help="to provide every detail of the airport")
    return vars(parser.parse_args())

def main(args):
    # url for subentity search with term=GB, local=en-US, active_only=False,location_types=airport and limit=999
    API_URL = "https://api.skypicker.com/locations?type=subentity&term=GB&locale=en-US&active_only=false&location_types=airport&limit=999"
    raw = get_data(API_URL)
    data = process_data(raw, args)

if __name__ == "__main__":
    args = parse_arguments()
    main(args)