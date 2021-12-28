from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from ConfigAPI.core import app
from flask import Flask
from sqlalchemy import and_,func,desc


import model_FDB as DBS
from model_FDB import  DB as DB_F
from CollectionOfQueries import QS

def test1():
    # table = DBS.classev_input_F
    # table = DBS.classpv_input_F
    table = DBS.classbess_parameter_input_F
    # table = DBS.classoutput_F
    # table = DBS.classnumberofst_output_F
    obj = QS.read(DB_F, table)
    # obj=table.query.all()
    return obj

def test_w1_outputac(Dict,NoS):
    table = DBS.classoutput_accepted_F
    crit = and_(DBS.classoutput_accepted_F.FK_numberofst_acepted == NoS)
    obj = QS.update_multiple_row(DB_F, table, Dict, crit)
    return obj

def test_w1_input(Dict,NoS):
    table = DBS.classtypeofinputt_F
    crit = and_(DBS.classtypeofinputt_F.FK_NumberOfSet_input == NoS)
    obj = QS.update_multiple_row(DB_F, table, Dict, crit)
    return obj

def test_w1_output(Dict,NoS):
    table = DBS.classoutput_F
    crit = and_(DBS.classoutput_F.FK_NumberOfSet_output == NoS)
    obj = QS.update_multiple_row(DB_F, table, Dict, crit)
    return obj

def test_w1_ev(Dict,NoS):
    table = DBS.classev_input_F
    crit = and_(DBS.classev_input_F.FK_numberofset_ev == NoS)
    obj = QS.update_multiple_row(DB_F, table, Dict, crit)
    return obj

def test_w1_pv(Dict,NoS):
    table = DBS.classpv_input_F
    crit = and_(DBS.classpv_input_F.FK_NumberOfSet_PV == NoS)
    obj = QS.update_multiple_row(DB_F, table, Dict, crit)
    return obj

def test_w1_dem(Dict,NoS):
    table = DBS.classdemand_input_F
    crit = and_(DBS.classdemand_input_F.FK_numberOfset_de == NoS)
    obj = QS.update_multiple_row(DB_F, table, Dict, crit)
    return obj

def test_r1_output(NoS):
    table = DBS.classoutput_F
    crit = DBS.classoutput_F.FK_NumberOfSet_output == NoS
    order = DBS.classoutput_F.timestamp.asc()
    obj = QS.read_filter(DB_F,table, crit, ordered = order)    
    return obj

def test_r1_input(NoS):
    table = DBS.classtypeofinputt_F
    crit = DBS.classtypeofinputt_F.FK_NumberOfSet_input == NoS
    order = DBS.classtypeofinputt_F.timestamp.asc()
    obj = QS.read_filter(DB_F,table, crit, ordered = order)    
    return obj

def Dict():
    lisp = []
    lisq = []
    for i in range(72):
        lisp.append(100+i)
        lisq.append(200+i)
    dict = {
        "P_Power_schedule":lisp,
        "Q_Power_schedule":lisq
        }
    # for i in range(72):
    #     dict["P_Power_schedule"[i] = 1]
    return dict


DictEV = {
    # "forecast":[0]*8+[10]*8+[0]*8+[0]*8+[10]*8+[0]*8+[0]*8+[10]*8+[0]*8
    "forecast":[0]*72
    }

DictPV = {
    # "forecast":[0]*8+[20]*8+[0]*8+[0]*8+[20]*8+[0]*8+[0]*8+[20]*8+[0]*8
    "forecast":[0, 0, 0, 0, 0, 10, 12, 18, 24, 30, 34, 36.8, 40, 40, 38, 36, 30, 24, 8, 4, 0, 0, 0, 0]*3
    # "forecast":[0]*72
    }

DictDem = {
    "forecast_P":[28, 35, 42, 49, 63, 105, 119, 112, 119, 120.4, 133, 140, 140, 131.6, 126, 112, 86.8, 77, 63, 56, 44.8, 35, 30.8, 28]*3,
    "forecast_Q":[0]*72
    }

DictERMS = {
    "forecast_P_price_up"           : [0]*72,
    "forecast_P_price_down"         : [0]*72,
    "forecast_Q_price_up"           : [0]*72,
    "forecast_Q_price_down"         : [0]*72,
    "Requirement_P_reserve_up"      : [0]*72,
    "Requirement_P_reserve_down"    : [0]*72,
    "Requirement_Q_reserve_up"      : [0]*72,
    "Requirement_Q_reserve_down"    : [0]*72,
    "Max_limit"                     : [100]*72,
    "Min_limit"                     : [0]*72,
    "P_forecast_price"              : [1.9748, 1.2046, 1.2045, 1.2046, 1.9043, 2.0906, 2.524, 3.30, 3.4498, 3.3002, 3.133, 3.00, 2.9472, 3.00, 3.28, 3.4218,3.5092,3.85,3.6213,3.4502,3.0333,2.6268,2.2594,2.0612]*3,
    # "P_forecast_price"              : [0]*72,
    "Q_forecast_price"              : [0]*72
    }

DictOutput = {
    "P_reserve_up"     : [0]*72, 
    "P_reserve_down"   : [0]*72,         
    "Q_reserve_up"     : [0]*72,   
    "Q_reserve_down"   : [0]*72,   
    "P_Bid_price_up"   : [0]*72,   
    "P_Bid_price_down" : [0]*72,   
    "Q_Bid_price_up"   : [0]*72,   
    "Q_Bid_price_down" : [0]*72,   
    "P_Power_schedule" : [0]*72,   
    "Q_Power_schedule" : [0]*72
    }

DictOutput_ac = {
    # "Dispatch_P": [0]*4+[50]*4+[0]*8+[0]*4+[-50]*4+[0]*4+[50]*4+[0]*8+[0]*4+[-50]*4+[0]*4+[50]*4+[0]*8+[0]*4+[-50]*4,
    "Dispatch_P": [0]*72, 
    "Dispatch_Q": [0]*72,
    "Ofered_P_reserve_up": [0]*72,
    "Ofered_P_Power_accepted": [0]*72,
    "Ofered_Q_Power_accepted": [0]*72,
    "Ofered_P_reserve_down": [0]*72,
    "Ofered_Q_reserve_up": [0]*72,
    "Ofered_Q_reserve_down": [0]*72,
    "Ofered_Price_P_Reserve_up": [0]*72,
    "Ofered_Price_Q_Reserve_up": [0]*72,
    "Ofered_Price_P_Reserve_down": [0]*72, 
    "Ofered_Price_Q_Reserve_down": [0]*72, 
    "Dispatch_P_reserve_up": [0]*72, 
    "Dispatch_P_reserve_down": [0]*72, 
    "Dispatch_Q_reserve_up" : [0]*72, 
    "Dispatch_Q_reserve_down" : [0]*72, 
    "Final_Price_P_Reserve_up" : [0]*72, 
    "Final_Price_P_Reserve_down" : [0]*72, 
    "Final_Price_Q_Reserve_up" : [0]*72, 
    "Final_Price_Q_Reserve_down" : [0]*72
    }

# obj2 = test_w1_output(DictOutput,1)
# obj2 = test_w1_input(DictERMS,1)
# obj2 = test_w1_outputac(DictOutput_ac,2)
# obj2 = test_w1_pv(DictPV,1)
# obj2 = test_w1_dem(DictDem,1)
# obj2 = test_w1_ev(DictEV,2)

newopt={
    "convergence": [1],
    "solution_time": [1.1],
    "objective_function": [1.5]
}
# print("\nConv = %d"%OPTResults.opt_conv)   
# print("\nTime = %s"%OPTResults.opt_time)   
# print("\nOF = %s"%OPTResults.OFval)   
# optresult=QS.write(DB_F,DBS.classoptimization_container_events_F,newopt)


# obj_bess = test1()
# obj1 = test1()
obj_o = test_r1_output(1)
# obj_i = test_r1_input(1)


# dict = Dict()
# a = test2(dict)

# def trying():
#     a = {"Hola2":"Hola","Hola3":"Hola"}
#     return a
# json1 = {}
# # json2 = {"Hola2":"Hola","Hola3":"Hola"}
# json1.update(trying())
# print(json1)
FMT = '%Y-%m-%d-%H:%M'
# init_t = datetime.now()
# init_t2 = datetime.strftime(init_t, FMT)
# print(init_t)
# print(init_t2)
# time_last_opt = datetime.strptime(last_opt[0].timestamp, '%Y-%m-%d %H:%M:%S')


if 'obj_bess' in locals(): 
    for object in obj_bess:
        psm = object.Power_limit
        nin = object.injection_eff
        nab = object.absortion_eff
        nsd = object.self_discharge
        ein = object.initial_energy
        elu = object.energy_upper_limit
        ell = object.energy_lower_limit
    f = open("guru99.txt","w+")
    f.write("Number of items \t%d\n"     % (len(obj_bess)))
    f.write("Power_limit         \t%.3f\n" % (psm))
    f.write("injection_eff       \t%.3f\n" % (nin))
    f.write("absortion_eff       \t%.3f\n" % (nab))
    f.write("self_discharge      \t%.3f\n" % (nsd))
    f.write("initial_energy      \t%.3f\n" % (ein))
    f.write("energy_upper_limit  \t%.3f\n" % (elu))
    f.write("energy_lower_limit  \t%.3f\n" % (ell))
    f.write("\n")
    f.close()

if 'obj_o' in locals(): 
    tsp = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []
    a8 = []
    a9 = []
    a10 = []
    a11 = []
    Nst = []
    for object in obj_o:
        tsp.append(datetime.strftime(object.timestamp, FMT))  
        # a1.append([object.forecast])  
        a1.append([object.P_Power_schedule])  
        a2.append([object.Q_Power_schedule])
        a3.append([object.P_reserve_up])
        a4.append([object.P_reserve_down])
        a5.append([object.Q_reserve_up])
        a6.append([object.Q_reserve_down])
        a7.append([object.P_Bid_price_up])
        a8.append([object.P_Bid_price_down])
        a9.append([object.Q_Bid_price_up])
        a10.append([object.Q_Bid_price_down])
        a11.append([object.Initial_Energy_schedule])
        Nst.append([object.FK_NumberOfSet_output])

    f= open("guru99.txt","w+")
    f.write("Number of items \t%d\n\n" % (len(obj_o)))
    f.write("i\t\t t.s\t\t\t\t a1\t\t\t a2\t\t\t a3\t\t\t a4\t\t \
        Nst\n") #a5\t\t\t a6\t\t\t a7\t\t\t a8\t\t\t a9\t\t\t a10\t\t\t 
    for i in range(len(obj_o)):
        f.write("%d\t\t" % (i))
        f.write("%s\t\t" % (tsp[i]))
        f.write("%s\t\t" % (a1[i]))
        f.write("%s\t\t" % (a2[i]))
        f.write("%s\t\t" % (a3[i]))
        f.write("%s\t\t" % (a4[i]))
        # f.write("%s\t\t" % (a5[i]))
        # f.write("%s\t\t" % (a6[i]))
        # f.write("%s\t\t" % (a7[i]))
        # f.write("%s\t\t" % (a8[i]))
        # f.write("%s\t\t" % (a9[i]))
        # f.write("%s\t\t" % (a10[i]))
        f.write("%s\t\t" % (a11[i]))
        f.write("%s\t\t" % (Nst[i]))
        f.write("\n")
    f.close()

if 'obj_i' in locals(): 
    tsp = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    a7 = []
    a8 = []
    a9 = []
    a10 = []
    Nst = []
    for object in obj_i:
        tsp.append(datetime.strftime(object.timestamp, FMT))  
        a1.append([object.P_forecast_price])  
        a2.append([object.Q_forecast_price])
        a3.append([object.Max_limit])
        a4.append([object.Min_limit])
        # a5.append([object.])
        # a6.append([object.])
        # a7.append([object.])
        # a8.append([object.])
        # a9.append([object.])
        # a10.append([object.])
        Nst.append([object.FK_NumberOfSet_input])

    f= open("guru98.txt","w+")
    f.write("Number of items \t%d\n\n" % (len(obj_i)))
    f.write("i\t\t t.s\t\t\t\t a1\t\t\t a2\t\t\t a3\t\t\t a4\t\t \
              Nst\n") #        a5\t\t\t a6\t\t\t a7\t\t\t a8\t\t\t a9\t\t\t a10\t\t\t \
    for i in range(len(obj_i)):
        f.write("%d\t\t" % (i))
        f.write("%s\t\t" % (tsp[i]))
        f.write("%s\t\t" % (a1[i]))
        f.write("%s\t\t" % (a2[i]))
        f.write("%s\t\t" % (a3[i]))
        f.write("%s\t\t" % (a4[i]))
        # f.write("%s\t\t" % (a5[i]))
        # f.write("%s\t\t" % (a6[i]))
        # f.write("%s\t\t" % (a7[i]))
        # f.write("%s\t\t" % (a8[i]))
        # f.write("%s\t\t" % (a9[i]))
        # f.write("%s\t\t" % (a10[i]))
        f.write("%s\t\t" % (Nst[i]))
        f.write("\n")
    f.close()
