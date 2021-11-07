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
from models import AMPL_dat_DBs,AMPL_res_DBs
from pprint import pprint
from teste import *


json_in = JSON_prov()
# print(json_in.keys())

def optimization_ERMS(json_in):
    # genera json input de prueba
    
    print('\n\n\n\n\n')
    # print(json_in)

    # genera AMPL Input 

    # # Input de prueba
    # InputClass1 = AMPLprov_dat() # test data

    # # Input from DBs
    OPTResults = OPTResults_prov()
    InputClass = AMPL_dat_DBs(json_in)
    """
    if 1:
        # print(InputClass.__dict__ == InputClass1.__dict__)
        # print(InputClass.__dict__ )
        # print(InputClass1.__dict__ )
        # Correr solver
        OPTResults = RUNAMPL(InputClass1)
        json_prueba = {'P_s':OPTResults.P_s, 'Q_s':OPTResults.Q_s}
        print(OPTResults.P_s)
        # print(OPTResults.Q_s)

        # Accesar DBs para escribir resultado
        if(json_in["ERMS_req"] == 1):
            OPTResults.ERMS_o = None#'1' # how to generate numberofset?
        else: 
            OPTResults.ERMS_o = None
        if(json_in["mCM_req"] == 1):
            OPTResults.mCM_o = '2' # how to generate numberofset?
        else: 
            OPTResults.mCM_o = None
        if(json_in["mFRR_req"] == 1):
            OPTResults.mFRR_o = '2' # how to generate numberofset?
        else: 
            OPTResults.mFRR_o = None
        if(json_in["aFRR_req"] == 1):
            OPTResults.aFRR_o = '2' # how to generate numberofset?
        else: 
            OPTResults.aFRR_o = None
        if(json_in["aCM_req"] == 1):
            OPTResults.aCM_o = '2' # how to generate numberofset? 
        else: 
            OPTResults.aCM_o = None   

        # generar json output
        #json={"Ps":OPTResults.P_s, "Q_s":OPTResults.Q_s}
        OPTResults.input_string = (  \
            str(json_in["ERMS_i"])+ ',' + \
            str(json_in["mCM_i"])+  ',' + \
            str(json_in["mFRR_i"])+ ',' + \
            str(json_in["aFRR_i"])+ ',' + \
            str(json_in["aCM_i"])+  ',' + \
            str(json_in["PV_i"])+   ',' + \
            str(json_in["EV_i"])+   ',' + \
            str(json_in["Dem_i"])+  ',' + \
            str(json_in["LEC_i"])    \
            )
        # OPTResults.input_string = 'string'
        json_out = JSON_out(OPTResults, json_in)
        # json_out = {"out":1}

        # subir resultados a la DBs
        # AMPL_res_DBs(json_out, OPTResults)
    """

    OPTResults = OPTResults_prov()
    json_out = JSON_out(OPTResults, json_in)
    res = AMPL_res_DBs(json_out, OPTResults)
    
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f= open("guru99.txt","w+")
    f.write("\nSolved at \t%s\n\n" % (dt_string))
    f.close()
    return json_out

# [x, y, res] = optimization_ERMS(json_in)

# print(y.p_pv)


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
