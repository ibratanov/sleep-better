#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:56:44 2023

@author: jikimji
"""

import requests
import json
from datetime import date, timedelta


class OuraActivityAgent:

    
    def get_activity_data(self):
        url = 'https://api.ouraring.com/v2/usercollection/daily_activity' 
        
        #end_date = date.today()
        end_date = date(2022, 4, 10)
        
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
            #print(response.text)
        return data
