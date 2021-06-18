#!/usr/bin/python3


import requests as rq
import argparse




result = rq.get('https://api.publicapis.org/entries')


result = result.json()


print(result)













