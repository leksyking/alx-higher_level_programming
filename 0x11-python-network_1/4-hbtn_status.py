#!/usr/bin/python3
"""
Module using request that fetches https://intranet.hbtn.io/status
"""
import requests


def main():
    """
    Function that fetches https://intranet.hbtn.io/status
    """
    url = 'https://intranet.hbtn.io/status'
    with requests.get(url) as r:
        print('Body response:')
        print('\t- type: {}'.format(type(r.text)))
        print('\t- content: {}'.format(r.text))


if __name__ == "__main__":
    main()
