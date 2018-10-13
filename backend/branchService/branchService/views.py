from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

def extract_time(request):
    url = 'http://127.0.0.1:8000/parse'
    print(request.GET)
    data = {
        'locale': request.GET.get('locale', ['en_GB'])[0],
        'tz': request.GET.get('tz', ['Asia/Shanghai'])[0],
        'text': request.GET.get('text')
    }
    resp = requests.post(url, data=data)
    js = json.loads(resp.content[1:-1])
    result = js['value']['values'][0]['value']

    return HttpResponse(result)
