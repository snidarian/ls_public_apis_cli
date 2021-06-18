#!/usr/bin/python3


import requests as rq
import json as j



result = rq.get('https://api.publicapis.org/entries')


data_object = result.json()


json_string = j.dumps(data_object, indent=2, ensure_ascii=False)



print(json_string)









