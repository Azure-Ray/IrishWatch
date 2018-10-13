from django.shortcuts import render
from django.http import HttpResponse

import requests
from urllib.parse import quote
from datetime import datetime


common_headers = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'Connection': 'keep-alive',
    'Content-Type': 'application/edn',
    'Host': 'duckling.wit.ai',
    'Referer': 'https://duckling.wit.ai/',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
}

def extract_time(request):
    url = 'https://duckling.wit.ai/parse/en$core/{}/-480/{}'
    obj = datetime.now()
    print(obj, obj.hour)
    time_now = '{}{}{}T{}{}{}'.format(obj.year, obj.month, obj.day, obj.hour, obj.minute, obj.second)
    request_url = url.format(time_now, quote(request.GET.get('time')))
    resp = requests.get(request_url, headers=common_headers)
    print(resp.content)
    print(resp.json())
    return HttpResponse(request)
