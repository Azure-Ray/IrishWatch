#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>

import requests

from .secret import subscription_key
#curl -X POST "https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?language=en-us&format=detailed" -H "Transfer-Encoding: chunked" -H "Ocp-Apim-Subscription-Key: YOUR_SUBSCRIPTION_KEY" -H "Content-type: audio/wav; codec=audio/pcm; samplerate=16000" --data-binary @YOUR_AUDIO_FILE

url = "https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?language=en-us&format=detailed"
headers = {
    "Transfer-Encoding": "chunked",
    "Content-type": "audio/wav; codec=audio/pcm; samplerate=16000",
    "Ocp-Apim-Subscription-Key": ""
}

def speech_to_text(audio):
    with open(audio, 'rb') as fd:
        data = fd.read()
    resp = requests.post(url,
            headers=headers,
            data=data)
    return resp.json()

