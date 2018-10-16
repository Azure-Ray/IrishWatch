from django.shortcuts import render
from django.http import HttpResponse

from . import duckling
from . import sentiment
from . import speech_to_text

import time
import json
import redis
redis_conn = redis.StrictRedis(host='127.0.0.1', port=6379)

def parse(request):
    print(request.GET)
    result = duckling.extract_time(request.GET)

    text = request.GET.get('text')
    result['polarity'] = sentiment.analysis_sentiment(text)

    return HttpResponse(json.dumps(result))


def speech(request):
    print(request.GET)

    # speech to text
    binary = request.GET.get('audio')
    js = speech_to_text.speech_to_text(binary)
    data['text'] = js['NBest'][0]['Display']

    # extract time and sentiment
    result = duckling.extract_time(data)
    result['polarity'] = sentiment.analysis_sentiment(data['text'])

    # branch info
    result['Identification'] = request.GET.get('Identification')
    result['branchName'] = request.GET.get('branchName')
    result['telephone'] = request.GET.get('telephone') # List

    # get date time from redis
    date = redis_conn.hget(result['Identification'], 'date')
    if date:
        timestamp = redis_conn.hset(result['Identification'], 'timestamp')
        if time.time() - float(timestamp) < 120:
            result['date'] = date

    hour_min = redis_conn.hget(result['Identification'], 'time')
    if hour_min:
        timestamp = redis_conn.hset(result['Identification'], 'timestamp')
        if time.time() - float(timestamp) < 120:
            result['time'] = hour_min

    show = analysis(result)
    return HttpResponse(show)


def analysis(result):
    artifical = ''
    if result['polarity'] != 'neutral' or result['polarity'] != 'positive':
        # or Please find the telephone contact form of the branch on the details page.
        artifical = 'You can also contact with the {} branch with a phone call: {}'.format(
                result['branchName'],
                ', '.join(result['telephone']))

    if 'date' not in result:
        show = 'Please tell me which day you\'d like to make the appointment. ' + artifical
        if 'time' in result:
            redis_conn.hset(result['Identification'], 'time', result['time'])
            redis_conn.hset(result['Identification'], 'timestamp', time.time())

    elif 'time' not in result:
        show = 'Please tell me the exact time you\'d like to make an appointment. ' + artifical
        if 'date' in result:
            redis_conn.hset(result['Identification'], 'date', result['date'])
            redis_conn.hset(result['Identification'], 'timestamp', time.time())

    else:
        show = 'Let me confirm the appointment with you. Branch {} in {} {}. '.format(
                result['branchName'],
                result['date'],
                result['time']) + artifical

    return show
