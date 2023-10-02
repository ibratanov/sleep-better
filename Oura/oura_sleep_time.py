#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:18:42 2023

@author: jikimji
"""

import requests
import json
from datetime import date, timedelta

#avg breathing rate, avg heart rate, average hrv, awake time, bedtime, etc with higher granularity 
url = 'https://api.ouraring.com/v2/usercollection/sleep_time' 

today = date.today()

params={ 
    'start_date': today - timedelta(days=10), 
    'end_date': today 
}
headers = { 
  'Authorization': 'Bearer 22SDZO557QZKJECZTE5MCZF4FAKI42BL' 
}
response = requests.request('GET', url, headers=headers, params=params) 
json_str = response._content.decode('utf-8')
my_dict = json.loads(json_str)
#data = my_dict['data'][0]
print(response.text)