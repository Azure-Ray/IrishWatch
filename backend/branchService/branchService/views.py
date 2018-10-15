from django.shortcuts import render
from django.http import HttpResponse

from . import duckling
from . import sentiment
from . import speech_to_text

import json

def parse(request):
    result = {}
    print(request.GET)
    result.update( duckling.extract_time(request.GET) )

    text = request.GET.get('text')
    result['polarity'] = sentiment.analysis_sentiment(text)

    return HttpResponse(json.dumps(result))


def speech(request):
    print(request.GET)
    binary = request.GET.get('audio')
    speech_to_text.speech_to_text(binary)

