# -*- coding: utf-8 -*-
"""
Created on Wed May 26 08:53:40 2021
@author: Carlos
"""
#from amplpy import AMPL, DataFrame  	# Importar objeto AMPL de libreria amplpy
#import pandas as pd      	# Importar pandas 
# from AMPL_func import AMPLdat_inputDF, AMPLprov_dat, RUNAMPL
from JSON_create import *
from flask import Flask,jsonify,request
#import pyutilib.subprocess.GlobalData
from datetime import datetime
import time
from pprint import pprint
from teste import *
from methods_dev import optimization_ERMS

json_in = JSON_prov()
# print(json_in.keys())

# x = optimization_ERMS(json_in)

# print(x)



# @app.route('/info', methods=['GET'])
# def get_info_direct_query():
#    json=resolver(request.json)
#    return json
# #
# @app.route('/pong', methods=['GET'])
# def get_info_direct_query():
#    return json_out
# #
# if __name__=="__main__":
#    app.run(host='0.0.0.0',debug=True,port=5000)
