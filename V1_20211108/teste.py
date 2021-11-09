from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from ConfigAPI.core import app
from flask import Flask
from sqlalchemy import and_,func,desc


import model_FDB as DBS
from model_FDB import  DB as DB_F
from CollectionOfQueries import QS

def test1():
    # table = DBS.classev_input_F
    # table = DBS.classpv_input_F
    table = DBS.classoutput_F
    # table = DBS.classnumberofst_output_F
    obj = QS.read(DB_F, table)
    return obj

def test2(Dict):
    table = DBS.classoutput_F
    crit = and_(DBS.classoutput_F.FK_NumberOfSet_output == 3)
    # crit = and_(DBS.classoutput_F.FK_NumberOfSet_output == 3, DBS.classoutput_F.timestamp >= time_first)
    # obj = QS.read_relationTable(DB_F,table,crit,secTable)
    obj = QS.update_multiple_row(DB_F,table, Dict, crit, ordered= None)
    # obj = QS.update_multiple_row(DB_F,table, Dict, DBS.classoutput_F.FK_NumberOfSet_output == 3, ordered= None)
    return obj

def test3():
    table=DBS.classnumberofst_output_F
    crit=DBS.classnumberofst_output_F.TypeOfOutput == "ERMS"
    # order = DBS.classnumberofst_output_F.timestamp.asc()
    # obj = QS.read_filter(DB_F,table, crit, ordered = order)
    # obj = QS.read_filter(DB_F,table, crit)
    obj = QS.read_filter(DB_F,DBS.classnumberofst_output_F, DBS.classnumberofst_output_F.TypeOfOutput == "ERMS")
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

obj1 = test3()
id_empty = []
early_timestamp = datetime.now()
for obj in obj1:    #for each result in previous query
    last_opt = QS.read_filter(DB_F, DBS.classoptimization_container_events_F, DBS.classoptimization_container_events_F.FK_NumberofSet_Output == obj.id_NumberofSet_Output, ordered = DBS.classoptimization_container_events_F.timestamp.desc())   #get last optimization done for that NumbofSet 
    if len(last_opt) == 0:
        id_empty.append(obj.id_NumberofSet_Output)
        print(id_empty)
    else:
        # print(last_opt[0].timestamp)
        # time_last_opt = datetime.strptime(last_opt[0].timestamp, '%Y-%m-%d %H:%M:%S')
        print(last_opt[0].timestamp)
        if last_opt[0].timestamp < early_timestamp:    #if last optimization timestamp occurred before than early_timestamp variable
            early_timestamp = last_opt[0].timestamp    #save last_opt timestamp in early_timestamp
            id = obj.id_NumberofSet_Output          #save number of set value as it is the "oldest"
to_optimize_json = {}


# dict = Dict()
# a = test2(dict)

# early_timestamp = datetime.now()
# print (early_timestamp)

# time_last_opt = datetime.strptime(last_opt[0].timestamp, '%Y-%m-%d %H:%M:%S')

"""
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
for object in obj1:
    tsp.append([object.timestamp])  
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
    Nst.append([object.FK_NumberOfSet_output])

f= open("guru99.txt","w+")
f.write("Number of items \t%d\n\n" % (len(obj1)))
f.write("i\t\t a1\t\t\t a2\t\t\t a3\t\t\t a4\t\t\t \
    a5\t\t\t a6\t\t\t a7\t\t\t a8\t\t\t a9\t\t\t a10\t\t\t Nst\n")
for i in range(len(obj1)):
    f.write("%d\t\t" % (i))
    f.write("%s\t\t" % (a1[i]))
    f.write("%s\t\t" % (a2[i]))
    f.write("%s\t\t" % (a3[i]))
    f.write("%s\t\t" % (a4[i]))
    f.write("%s\t\t" % (a5[i]))
    f.write("%s\t\t" % (a6[i]))
    f.write("%s\t\t" % (a7[i]))
    f.write("%s\t\t" % (a8[i]))
    f.write("%s\t\t" % (a9[i]))
    f.write("%s\t\t" % (a10[i]))
    f.write("%s\t\t" % (Nst[i]))
    f.write("\n")
f.close()
"""