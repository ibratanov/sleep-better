#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:18:42 2023

@author: jikimji
"""

import requests
import json


class OuraAgent:
    def get_daily_sleep_data(self):
        #gives scores for deep sleep, efficiency, latency, rem_sleep, restfulness, timing, total sleep
        #on each day - out of 100
        url = 'https://api.ouraring.com/v2/usercollection/daily_sleep' 


        params={ 
            'start_date': '2023-09-30', 
            'end_date': '2023-10-01' 
        }
        headers = { 
          'Authorization': 'Bearer 22SDZO557QZKJECZTE5MCZF4FAKI42BL' 
        }
        response = requests.request('GET', url, headers=headers, params=params) 
        json_str = response._content.decode('utf-8')
        my_dict = json.loads(json_str)
        data = my_dict['data'][0]
        #print(response.text)
        return response.text
    
    def get_sleep_data(self):
        #get higher detailed sleeping data: i.e. avg breathing rate, avg heart rate, average hrv, awake time, bedtime 
        url = 'https://api.ouraring.com/v2/usercollection/sleep' 

        params={ 
            'start_date': '2023-09-30', 
            'end_date': '2023-10-01' 
        }
        headers = { 
          'Authorization': 'Bearer 22SDZO557QZKJECZTE5MCZF4FAKI42BL' 
        }
        response = requests.request('GET', url, headers=headers, params=params) 
        json_str = response._content.decode('utf-8')
        my_dict = json.loads(json_str)
        data = my_dict['data'][0]
        print(response.text)
        return response.text