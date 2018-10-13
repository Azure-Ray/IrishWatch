from django.shortcuts import render
from django.http import HttpResponse

import requests

def extract_time(request):
    url = 'https://duckling.wit.ai/parse/en$core/20181013T133054/-480/'
    print(request)
    return HttpResponse(request)
    'I\'d%20like%20to%20have%20an%20appointment%20at%20half%20ten%20tomorrow'
