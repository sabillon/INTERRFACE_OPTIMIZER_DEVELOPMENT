from flask import Blueprint, json, request, make_response, jsonify
from flask.views import MethodView
from datetime import datetime
from sqlalchemy import and_,func,desc
import requests
from JSON_create import *

#%% # DB Loading
import model_FDB as DBS
from model_FDB import  DB as DB_F
from CollectionOfQueries import QS

#%% # Publishing
test_blueprint = Blueprint('test', __name__)

#%% AMPL Input / Output Functions
"""
# =================================================================================================
# Conection AMPL - Python
# ================================================================================================
"""

# def AMPL_dat_DBs(json_in):
#     # Consult DBs
#     # ip_EM="127.0.0.1:5000"
#     # ip_EM="172.16.239.2:5000"
#     # response = requests.get("http://"+ip_EM+"/DB_Autoritzation",json={"activity":'Read', "DB":'FDB'})
#     ax = 1
#     # if response.json()["Acces"] == 'True' :
#     if ax == 1 :
#         # print('\n\n FDB access granted \n')    
#         # T
#         FMT = '%Y-%m-%d-%H:%M'
#         FMTS = '%H:%M'
#         time_diff = datetime.strptime(json_in['Final_time'], FMT) - datetime.strptime(json_in['Init_time'], FMT)
#         time_step = datetime.strptime(json_in['Time_step'], FMTS)
#         time_step_sec = time_step.hour * 3600 + time_step.minute * 60
#         Number_of_intervals = (time_diff.days*24*3600 + time_diff.seconds)/time_step_sec + 1
        
#         # Read PV
#         table = DBS.classpv_input_F
#         crit = DBS.classpv_input_F.FK_NumberOfSet_PV == json_in['PV_i']
#         order = DBS.classpv_input_F.timestamp.asc()
#         Set_of_obj_p_pv = QS.read_filter(DB_F,table, crit, ordered = order)

#         # Read Demand
#         table = DBS.classdemand_input_F
#         crit = DBS.classdemand_input_F.FK_numberOfset_de == json_in['Dem_i']
#         order = DBS.classdemand_input_F.timestamp.asc()
#         Set_of_obj_p_l = QS.read_filter(DB_F,table, crit, ordered = order)
       
#         # Read EV
#         table = DBS.classev_input_F
#         crit = DBS.classev_input_F.FK_numberofset_ev == json_in['EV_i']
#         order = DBS.classev_input_F.timestamp.asc()
#         Set_of_obj_p_e = QS.read_filter(DB_F,table, crit, ordered = order)

#         # Read LEC
#         table = DBS.classlec_F
#         crit = DBS.classlec_F.FK_numberofst_lec == json_in['LEC_i']
#         order = DBS.classlec_F.timestamp.asc()
#         Set_of_obj_p_lec = QS.read_filter(DB_F,table, crit, ordered = order)

#         # Read ERMS
#         if json_in['ERMS_req'] == 0:
#             a = "empty"
            
#         elif json_in['ERMS_req'] == 1:
#             table=DBS.classtypeofinputt_F
#             crit=DBS.classtypeofinputt_F.FK_NumberOfSet_input == json_in['ERMS_i']
#             order = DBS.classtypeofinputt_F.timestamp.asc()
#             Set_of_obj_p_erms = QS.read_filter(DB_F,table, crit, ordered = order)

#         elif json_in['ERMS_req'] == 2:
#             table=DBS.classoutput_accepted_F
#             crit=DBS.classoutput_accepted_F.FK_NumberOfSet_input == json_in['ERMS_i']
#             order = DBS.classoutput_accepted_F.timestamp.asc()
#             Set_of_obj_p_erms = QS.read_filter(DB_F,table, crit, ordered = order)

#         # Read aFRR
#         if json_in['aFRR_req'] == 0:
#             a = "empty"
            
#         elif json_in['aFRR_req'] == 1:
#             table=DBS.classtypeofinputt_F
#             crit=DBS.classtypeofinputt_F.FK_NumberOfSet_input == json_in['aFRR_i']
#             order = DBS.classtypeofinputt_F.timestamp.asc()
#             Set_of_obj_p_aFRR = QS.read_filter(DB_F,table, crit, ordered = order)

#         elif json_in['aFRR_req'] == 2:
#             table=DBS.classoutput_accepted_F
#             crit=DBS.classoutput_accepted_F.FK_NumberOfSet_input == json_in['aFRR_i']
#             order = DBS.classoutput_accepted_F.timestamp.asc()
#             Set_of_obj_p_aFRR = QS.read_filter(DB_F,table, crit, ordered = order)

#         elif json_in['aFRR_req'] == 3:
#             table=DBS.classoutput_accepted_F
#             crit=DBS.classoutput_accepted_F.FK_NumberOfSet_input == json_in['aFRR_i']
#             order = DBS.classoutput_accepted_F.timestamp.asc()
#             Set_of_obj_p_aFRR = QS.read_filter(DB_F,table, crit, ordered = order)

#         # Read mFRR
#         if json_in['mFRR_req'] == 0:
#             a = "empty"
            
#         elif json_in['mFRR_req'] == 1:
#             table=DBS.classtypeofinputt_F
#             crit=DBS.classtypeofinputt_F.FK_NumberOfSet_input == json_in['mFRR_i']
#             order = DBS.classtypeofinputt_F.timestamp.asc()
#             Set_of_obj_p_mFRR = QS.read_filter(DB_F,table, crit, ordered = order)

#         elif json_in['mFRR_req'] == 2:
#             table=DBS.classoutput_accepted_F
#             crit=DBS.classoutput_accepted_F.FK_NumberOfSet_input == json_in['mFRR_i']
#             order = DBS.classoutput_accepted_F.timestamp.asc()
#             Set_of_obj_p_mFRR = QS.read_filter(DB_F,table, crit, ordered = order)

#         elif json_in['mFRR_req'] == 3:
#             table=DBS.classoutput_accepted_F
#             crit=DBS.classoutput_accepted_F.FK_NumberOfSet_input == json_in['mFRR_i']
#             order = DBS.classoutput_accepted_F.timestamp.asc()
#             Set_of_obj_p_mFRR = QS.read_filter(DB_F,table, crit, ordered = order)
        
#         # Read mCM
#         if json_in['mCM_req'] == 0:
#             a = "empty"
            
#         elif json_in['mCM_req'] == 1:
#             table=DBS.classtypeofinputt_F
#             crit=DBS.classtypeofinputt_F.FK_NumberOfSet_input == json_in['mCM_i']
#             order = DBS.classtypeofinputt_F.timestamp.asc()
#             Set_of_obj_p_mCM = QS.read_filter(DB_F,table, crit, ordered = order)

#         elif json_in['mCM_req'] == 2:
#             table=DBS.classoutput_accepted_F
#             crit=DBS.classoutput_accepted_F.FK_NumberOfSet_input == json_in['mCM_i']
#             order = DBS.classoutput_accepted_F.timestamp.asc()
#             Set_of_obj_p_mCM = QS.read_filter(DB_F,table, crit, ordered = order)

#         elif json_in['mCM_req'] == 3:
#             table=DBS.classoutput_accepted_F
#             crit=DBS.classoutput_accepted_F.FK_NumberOfSet_input == json_in['mCM_i']
#             order = DBS.classoutput_accepted_F.timestamp.asc()
#             Set_of_obj_p_mCM = QS.read_filter(DB_F,table, crit, ordered = order)
        
#         # Read aCM
#         if json_in['aCM_req'] == 0:
#             a = "empty"
            
#         elif json_in['aCM_req'] == 1:
#             table=DBS.classtypeofinputt_F
#             crit=DBS.classtypeofinputt_F.FK_NumberOfSet_input == json_in['aCM_i']
#             order = DBS.classtypeofinputt_F.timestamp.asc()
#             Set_of_obj_p_aCM = QS.read_filter(DB_F,table, crit, ordered = order)

#         elif json_in['aCM_req'] == 2:
#             table=DBS.classoutput_accepted_F
#             crit=DBS.classoutput_accepted_F.FK_NumberOfSet_input == json_in['aCM_i']
#             order = DBS.classoutput_accepted_F.timestamp.asc()
#             Set_of_obj_p_aCM = QS.read_filter(DB_F,table, crit, ordered = order)

#         elif json_in['aCM_req'] == 3:
#             table=DBS.classoutput_accepted_F
#             crit=DBS.classoutput_accepted_F.FK_NumberOfSet_input == json_in['aCM_i']
#             order = DBS.classoutput_accepted_F.timestamp.asc()
#             Set_of_obj_p_aCM = QS.read_filter(DB_F,table, crit, ordered = order)
        
#         """
#         """

#         class AMPLinput:
#             # Creation Flag
#             create = 1
#             Init_time = json_in["Init_time"]
#             Final_time = json_in["Final_time"]
#             # T
#             NT = Number_of_intervals
#             Times = range(1, int(Number_of_intervals))
#             dt = [time_step_sec / 60] * int(Number_of_intervals)
#             # Consumers
#             Consu = [1]
#             # EVs
#             EVs = [1]
#             # PV
#             p_pv = []
#             for object in Set_of_obj_p_pv:
#                 p_pv.append([object.forecast])  
#             """"
#             # Demand
#             p_l = []
#             q_l = []
#             for object in Set_of_obj_p_l:
#                 p_l.append([object.forecast_P])  
#                 q_l.append([object.forecast_Q])
#             # EVs
#             p_e = []
#             for object in Set_of_obj_p_e:
#                 p_e.append([object.forecast])    
#             # ke
#             ke = []
#             keq = []
#             for object in Set_of_obj_ke:
#                 ke.append([object.P_forecasted_price])          
#                 keq.append([object.Q_forecasted_price])          
#             # param
#             kdc = 0
#             nab = 0.7975
#             nin = 0.8829
#             nsd = 0
#             ein = 0
#             psm = 200
#             elu = 438
#             ell = 0
#             pim = 0
#             kadn = 0.0101439
#             katn = 0.0002295
#             ktmv = 0.004998
#             kttn = 0.005253
#             kqga = 0.058344
#             kqua = 0.0058344
#             print('\n\n FDB read succesfully \n')    
#             """
#     else :
#         print('Unable to access DBs for reading input')
#         class AMPLinput:
#             # Creation Flag
#             create = 0
#     return AMPLinput

# def AMPL_res_DBs(json_out, OPTResults):# Save DBs
#     # Consult DBs
#     # ip_EM="127.0.0.1:5000"
#     # ip_EM="172.16.239.2:5000"
#     # response = requests.get("http://"+ip_EM+"/DB_Autoritzation",json={"activity":'Read', "DB":'FDB'})
#     ax = 1
#     # if response.json()["Acces"] == 'True' :
#     if ax == 1 :
#         # print('\n\n FDB access granted \n')    
#         # writing ERMS    
#         if json_out['ERMS_req'] == 1:
#             Dict = Dict_ERMS() # prueba
#             table = DBS.classoutput_F
#             crit = and_(DBS.classoutput_F.FK_NumberOfSet_output == json_out['ERMS_o'])
#             obj = QS.update_multiple_row(DB_F,table, Dict, crit, ordered= None)
#         # writing aFRR    
#         if json_out['aFRR_req'] == 1:
#             Dict = Dict_aFRR() # prueba
#             table = DBS.classoutput_F
#             crit = and_(DBS.classoutput_F.FK_NumberOfSet_output == json_out['aFRR_o'])
#             obj = QS.update_multiple_row(DB_F,table, Dict, crit, ordered= None)
#         # writing mFRR    
#         if json_out['mFRR_req'] == 1:
#             Dict = Dict_mFRR() # prueba
#             table = DBS.classoutput_F
#             crit = and_(DBS.classoutput_F.FK_NumberOfSet_output == json_out['mFRR_o'])
#             obj = QS.update_multiple_row(DB_F,table, Dict, crit, ordered= None)
#         # writing mCM    
#         if json_out['mCM_req'] == 1:
#             Dict = Dict_mCM() # prueba
#             table = DBS.classoutput_F
#             crit = and_(DBS.classoutput_F.FK_NumberOfSet_output == json_out['mCM_o'])
#             obj = QS.update_multiple_row(DB_F,table, Dict, crit, ordered= None)
#         # writing aCM    
#         if json_out['aCM_req'] == 1:
#             Dict = Dict_aCM() # prueba
#             table = DBS.classoutput_F
#             crit = and_(DBS.classoutput_F.FK_NumberOfSet_output == json_out['aCM_o'])
#             obj = QS.update_multiple_row(DB_F,table, Dict, crit, ordered= None)
#     else :
#         print('Unable to access DBs for writing results')
    
#     """
#     ip_EM="172.16.239.2:5000"
#     response = requests.get("http://"+ip_EM+"/DB_Autoritzation",json={"activity":'Write', "DB":'FDB'})
#     if response.json()["Acces"] == 'True' :
#         print('\n\n FDB access granted \n')    
#         obj = classNumberOfSet_output(NumberOfSet_ERMS=None, NumberOfSet_AFrr=json_out["aFRR_o"], NumberOfSet_MFrr=json_out["mFRR_o"], NumberOfSet_MCM=json_out["mCM_o"], NumberOfSet_ACM=json_out["aCM_o"], NumberOfSet_pv=None, NumberOfSet_ev=None, NumberOfSet_de=None, NumberOfSet_LEC=None, TypeOfInput="ERMS")
#         DB.session.add(obj)
#         DB.session.commit()
#         for i in range(OPTResults.NT):
#             obj2=classOUTPUT(timestamp=OPTResults.timestamp_array[i], P_reserve_up=None, Q_reserve_up=None, P_reserve_down=None, Q_reserve_down=None, P_Bid_price_up=None, P_Bid_price_down=None, Q_Bid_price_up=None, Q_Bid_price_down=None, P_Power_schedule=OPTResults.P_s[i][1], Q_Power_schedule=OPTResults.Q_s[i][1], NumberofSet_Output=obj.NumberOfSet_output)
#             DB.session.add(obj2)
#         DB.session.commit()
#         print('\n\n FDB read succesfully \n')    
#     """    
  

#%% AMPL Call
def optimization_ERMS(json_in):
    """
    #%% AMPL INPUT
    OPTResults = OPTResults_prov()
    InputClass = AMPL_dat_DBs(json_in)
    
    #%% AMPL Output
    OPTResults = OPTResults_prov()
    json_out = JSON_out(OPTResults, json_in)
    res = AMPL_res_DBs(json_out, OPTResults)
    
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # f= open("guru99.txt","w+")
    # f.write("\nSolved at \t%s\n\n" % (dt_string))
    # f.close()
    """
    print(json_in)
    json_out = {"Rec": "True"}
    return json_out

   
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