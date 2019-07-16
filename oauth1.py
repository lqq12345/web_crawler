#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

auth = OAuth1()
