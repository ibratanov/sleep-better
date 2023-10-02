#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:18:42 2023

@author: jikimji
"""

import requests
import json
from datetime import date, timedelta


class OuraAgent:

    
    def get_sleep_data(self):
        #get higher detailed sleeping data: i.e. avg breathing rate, avg heart rate, average hrv, awake time, bedtime 
        url = 'https://api.ouraring.com/v2/usercollection/sleep' 
        
        #end_date = date.today()
        end_date = date(2023, 8, 10)

        params={ 
            'start_date': end_date - timedelta(days=7), 
            'end_date': end_date 
            }

        headers = { 
          'Authorization': 'Bearer 22SDZO557QZKJECZTE5MCZF4FAKI42BL' 
        }
        response = requests.request('GET', url, headers=headers, params=params) 
        json_str = response._content.decode('utf-8')
        my_dict = json.loads(json_str)
        data = my_dict['data']
        
        for i in range(len(data)):
            del data[i]['movement_30_sec']
            del data[i]['sleep_phase_5_min']
            del data[i]['heart_rate']
            del data[i]['hrv']
            del data[i]['id']
            del data[i]['low_battery_alert']
            del data[i]['readiness']
            del data[i]['sleep_algorithm_version']
        #print(response.text)
        return data
    
    def get_activity_data(self):
        url = 'https://api.ouraring.com/v2/usercollection/daily_activity' 
        
        #end_date = date.today()
        end_date = date(2023, 8, 10)
        
        params={ 
            'start_date': end_date - timedelta(days=1), 
            'end_date': end_date 
            }
        
        headers = { 
          'Authorization': 'Bearer 22SDZO557QZKJECZTE5MCZF4FAKI42BL' 
        }
        response = requests.request('GET', url, headers=headers, params=params) 
        json_str = response._content.decode('utf-8')
        my_dict = json.loads(json_str)
        data = my_dict['data']
            
        for i in range(len(data)):
            del data[i]['class_5_min']
            del data[i]['id']
            del data[i]['met']
            del data[i]['contributors']
            del data[i]['score']
            del data[i]['non_wear_time']
            del data[i]['timestamp']
            #print(response.text)
        return data
