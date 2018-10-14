#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>

from aylienapiclient import textapi

app_id = ""
app_key = ""
sentiment_client = textapi.Client(app_id, app_key)

def analysis_sentiment(text):
    s = sentiment_client.Sentiment({'text': text})
    #{'polarity': 'neutral', 'subjectivity': 'subjective', 'text': 'ten half of tomorrow morning', 'polarity_confidence': 0.6261608600616455, 'subjectivity_confidence': 0.9999999860809148}

    # positive neutral
    return s['polarity']
