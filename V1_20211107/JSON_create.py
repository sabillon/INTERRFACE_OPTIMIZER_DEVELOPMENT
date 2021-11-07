# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:07:26 2021

@author: Carlos
"""

from flask import Flask,jsonify,request

def JSON_prov():
    json = {
                "Source/Client": "IEGSA/IDNO", 
                "Type": "Process Enquiry", 
                "Date": "2021-06-01", 
                "Keyname": "Opt_Enq", 
                "Opt_type": 1, 
                "Init_time": "2021-06-01-00:00", 
                "Final_time": "2021-06-03-23:00", 
                "Time_step": "01:00", 
                "ERMS_req": 1, 
                "mCM_req": 1, 
                "mFRR_req": 1, 
                "aFRR_req": 1, 
                "aCM_req": 1, 
                "ERMS_i": 1, 
                "aFRR_i": 6, 
                "mFRR_i": 11, 
                "mCM_i": 16, 
                "aCM_i": 21, 
                "PV_i": 2, 
                "EV_i": 1, 
                "Dem_i": 1, 
                "LEC_i": None,
                "ERMS_o": 1, 
                "aFRR_o": 2, 
                "mFRR_o": 3, 
                "mCM_o": 4, 
                "aCM_o": 5 
            }
    return json

def JSON_out(OPTResults, json_in):
    json = {"Source/Client": json_in["Source/Client"]}
    json["Type"] = json_in["Type"]
    json["Type"] = json_in["Type"]
    json["Date"] = json_in["Date"] 	
    json["Keyname"] = json_in["Keyname"] 
    json["Opt_type"] = json_in["Opt_type"] 
    json["Init_time"] = json_in["Init_time"]
    json["Final_time"] = json_in["Final_time"]
    json["Time_step"] = json_in["Time_step"]
    json["ERMS_req"] = json_in["ERMS_req"] 
    json["mCM_req"] = json_in["mCM_req"] 
    json["mFRR_req"] = json_in["mFRR_req"] 
    json["aFRR_req"] = json_in["aFRR_req"] 
    json["aCM_req"] = json_in["aCM_req"] 
    json["ERMS_o"] = json_in["ERMS_o"]	
    json["mCM_o"] = json_in["mCM_o"]
    json["mFRR_o"] = json_in["mFRR_o"]
    json["aFRR_o"] = json_in["aFRR_o"]
    json["aCM_o"] = json_in["aCM_o"]
    json["input_ids"] = OPTResults.input_string
    json["opt_conv"] = OPTResults.opt_conv 
    json["opt_time"] = OPTResults.opt_time 
    return json


def OPTResults_prov():
    class OPTResults:
        # Creation Flag
        input_string = 1
        opt_conv = 1
        opt_time = 1
    return OPTResults


def Dict_ERMS():
    a = 45
    b = 100
    dict = {
        "P_Power_schedule" : list(range(a, a+72)),
        "Q_Power_schedule" : list(range(b, b+72))
        }
    return dict

def Dict_aFRR():
    a = 20
    dict = {
        "P_reserve_up" : list(range(a, a+72)),
        "P_reserve_down" : list(range(a, a+72)),
        "Q_reserve_up" : list(range(a, a+72)),
        "Q_reserve_down" : list(range(a, a+72)),
        "P_Bid_price_up" : list(range(a, a+72)),
        "P_Bid_price_down" : list(range(a, a+72)),
        "Q_Bid_price_up" : list(range(a, a+72)),
        "Q_Bid_price_down" : list(range(a, a+72))        
        }
    return dict

def Dict_mFRR():
    a = 200
    dict = {
        "P_reserve_up" : list(range(a, a+72)),
        "P_reserve_down" : list(range(a, a+72)),
        "Q_reserve_up" : list(range(a, a+72)),
        "Q_reserve_down" : list(range(a, a+72)),
        "P_Bid_price_up" : list(range(a, a+72)),
        "P_Bid_price_down" : list(range(a, a+72)),
        "Q_Bid_price_up" : list(range(a, a+72)),
        "Q_Bid_price_down" : list(range(a, a+72))        
        }
    return dict

def Dict_mCM():
    a = 300
    dict = {
        "P_reserve_up" : list(range(a, a+72)),
        "P_reserve_down" : list(range(a, a+72)),
        "Q_reserve_up" : list(range(a, a+72)),
        "Q_reserve_down" : list(range(a, a+72)),
        "P_Bid_price_up" : list(range(a, a+72)),
        "P_Bid_price_down" : list(range(a, a+72)),
        "Q_Bid_price_up" : list(range(a, a+72)),
        "Q_Bid_price_down" : list(range(a, a+72))        
        }
    return dict

def Dict_aCM():
    a = 400
    dict = {
        "P_reserve_up" : list(range(a, a+72)),
        "P_reserve_down" : list(range(a, a+72)),
        "Q_reserve_up" : list(range(a, a+72)),
        "Q_reserve_down" : list(range(a, a+72)),
        "P_Bid_price_up" : list(range(a, a+72)),
        "P_Bid_price_down" : list(range(a, a+72)),
        "Q_Bid_price_up" : list(range(a, a+72)),
        "Q_Bid_price_down" : list(range(a, a+72))        
        }
    return dict

# P_reserve_up = list(range(1, 5))
# P_reserve_down = list(range(1, 5))
# Q_reserve_up = list(range(1, 5))
# Q_reserve_down = list(range(1, 5))
# P_Bid_price_up = list(range(1, 5))
# P_Bid_price_down = list(range(1, 5))
# Q_Bid_price_up = list(range(1, 5))
# Q_Bid_price_down = list(range(1, 5))
# P_Power_schedule = list(range(1, 5))
# Q_Power_schedule = list(range(1, 5))

json1 = JSON_prov()
#json2 = JSON_out(1,json1)

print(json1["Type"])
    
