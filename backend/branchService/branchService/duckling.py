#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>

import requests
import json

def extract_time(request_get):
    result = {}
    duckling_url = 'http://127.0.0.1:8000/parse'
    text = request_get.get('text')

    data = {
        'locale': request_get.get('locale', ['en_GB'])[0],
        'tz': request_get.get('tz', ['Asia/Shanghai'])[0],
        'text': text
    }
    resp = requests.post(duckling_url, data=data)
    js = json.loads(resp.content[1:-1])
    print(js)

    content = js['value']['values'][0]
    if content['type'] == 'value':
        result['date'], result['time'] = content['value'].split('T')
    elif content['type'] == 'interval':
        result['date'], result['time'] = content['to']['value'].split('T')
    return result
