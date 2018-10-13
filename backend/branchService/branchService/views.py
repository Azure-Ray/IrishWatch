from django.shortcuts import render
from django.http import HttpResponse

from sentiment import sentiment_client

import requests
import json

def extract_time(request):
    url = 'http://127.0.0.1:8000/parse'
    text = request.GET.get('text')
    print(request.GET)
    data = {
        'locale': request.GET.get('locale', ['en_GB'])[0],
        'tz': request.GET.get('tz', ['Asia/Shanghai'])[0],
        'text': text
    }
    resp = requests.post(url, data=data)
    js = json.loads(resp.content[1:-1])
    result = js['value']['values'][0]['value']

    s = sentiment_client.Sentiment({'text': text})
    print(s)

    return HttpResponse(result)
