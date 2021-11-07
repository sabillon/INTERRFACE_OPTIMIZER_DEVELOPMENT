from flask import Blueprint, json, request, make_response, jsonify
from flask.views import MethodView
#from ConfigAPI.core import app
import datetime
import requests
from main import optimization_ERMS

test_blueprint = Blueprint('test', __name__)

"""
# =================================================================================================
# Conexão AMPL - Python
# ================================================================================================
"""
#%% 
#from amplpy import AMPL  	# Importar objeto AMPL de libreria amplpy
#import pandas as pd      	# Importar pandas 
#from json2dat import json2dat       
#import pyutilib.subprocess.GlobalData
#import time
#pyutilib.subprocess.GlobalData.DEFINE_SIGNAL_HANDLERS_DEFAULT = False
#
   
#%% Crear funcion para optimizar el modelo
class Optimitzation_ERMS(MethodView):
    def get(self):
        print(request.json)
        json_in = request.json
        json_prueba = optimization_ERMS(json_in)
        return json_prueba, 200


# response = requests.get("http://127.0.0.1:5001/DB_Autoritzation",json= json)
# response.json()["Acces"]
# requests.put

 
Optimitzation_ERMS_view = Optimitzation_ERMS.as_view('Optimitzation_ERMS_api')

test_blueprint.add_url_rule(
    '/Optimitzation_ERMS',
    view_func=Optimitzation_ERMS_view,
    methods=['GET'])