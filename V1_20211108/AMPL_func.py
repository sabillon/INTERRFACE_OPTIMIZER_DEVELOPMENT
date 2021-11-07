# -*- coding: utf-8 -*-
"""
Created on Wed May 26 08:53:40 2021

@author: Carlos
"""
from amplpy import AMPL, DataFrame  	# Importar objeto AMPL de libreria amplpy
import pandas as pd      	 # Importar pandas 
from datetime import datetime
import requests
import time

def AMPLprov_dat():
    response = requests.get("http://127.0.0.1:5000/DB_Autoritzation",json={"activity":'Read', "DB":'FDB'})
    if response.json()["Acces"] == 'True' :
        print('\n\n DBs access granted \n')    
        class AMPLinput:
            create = 1
            # Sets
            Times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,	28,	29,	30,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53,	54,	55,	56,	57,	58,	59,	60,	61,	62,	63,	64,	65,	66,	67,	68,	69,	70,	71,	72]
            Consu = [1]
            EVs = [1]

            # Param{T}
            dt = [1] * 72
            ke = [0.04]*8+[0.05]*8+[0.03]*8+[0.04]*8+[0.05]*8+[0.03]*8+[0.04]*8+[0.05]*8+[0.03]*8
            keq = [0.0]*72
            p_pv = [0]*8+[10]*8+[0]*8+[0]*8+[10]*8+[0]*8+[0]*8+[10]*8+[0]*8

            # Param{T,C}
            p_l = [110]*72
            q_l = [0]*72

            # Param{T,E}
            p_e = [0]*72

            # Param
            kdc = 0
            nab = 0.7975
            nin = 0.8829
            nsd = 0
            ein = 0
            psm = 200
            elu = 438
            ell = 0
            pim = 0
            kadn = 0.0101439
            katn = 0.0002295
            ktmv = 0.004998
            kttn = 0.005253
            kqga = 0.058344
            kqua = 0.0058344
            #
            NT = 72
            Init_time = "2021-06-01-00:00"
            Final_time = "2021-06-03-23:00"
        print('\n\n DBs read successfully \n\n')    
    else :
        class AMPLinput:
            create = 0  
        print('\n\n Unable to access DBs for reading input \n\n')    
    return AMPLinput


def AMPLdat_inputDF(InputClass):
    
    Lenght_Times = len(InputClass.Times)
    Lenght_Consu = len(InputClass.Consu)
    Lenght_EVs = len(InputClass.EVs)
        
    # Set T
    dfT = DataFrame('T')
    dfT.setColumn('T', InputClass.Times)
    # param dT
    dfT.addColumn('dt', InputClass.dt)
    # param ke
    dfT.addColumn('ke', InputClass.ke)
    # param PV
    dfT.addColumn('p_pv', InputClass.p_pv)
        
    # Set C
    dfC = DataFrame('C')
    dfC.setColumn('C', InputClass.Consu)
        
    # Set E
    dfE = DataFrame('E')
    dfE.setColumn('E', InputClass.EVs)
        
    #### params {T,C}
    dfT_C = DataFrame(index=('T', 'C'))
    # # Populate the set columns
    TWithMultiplicity = ['']*Lenght_Times*Lenght_Consu
    CWithMultiplicity = ['']*Lenght_Times*Lenght_Consu
    i = 0
    for n in range(Lenght_Times):
        for f in range(Lenght_Consu):
            TWithMultiplicity[i] = InputClass.Times[n]
            CWithMultiplicity[i] = InputClass.Consu[f]
            i += 1
    dfT_C.setColumn('T', TWithMultiplicity)
    dfT_C.setColumn('C', CWithMultiplicity)
    # # Populate with p_l
    dfT_C.addColumn('p_l', InputClass.p_l)	
    dfT_C.addColumn('q_l', InputClass.q_l)	
        
    ##### params {T,E}
    dfT_E = DataFrame(index=('T', 'E'))
    # # Populate the set columns
    TWithMultiplicity = ['']*Lenght_Times*Lenght_EVs
    EWithMultiplicity = ['']*Lenght_Times*Lenght_EVs
    i = 0
    for n in range(Lenght_Times):
        for f in range(Lenght_EVs):
            TWithMultiplicity[i] = InputClass.Times[n]
            EWithMultiplicity[i] = InputClass.EVs[f]
            i += 1
    dfT_E.setColumn('T', TWithMultiplicity)
    dfT_E.setColumn('E', EWithMultiplicity)
    # # Populate with p_l
    dfT_E.addColumn('p_e', InputClass.p_e)	
        
    return dfT, dfC, dfE, dfT_C, dfT_E

def RUNAMPL(InputClass):
    opt_t = time.time()
    ampl = AMPL()            	# Atribuir objeto AMPL() a variable
    ampl.reset()             	# Reiniciar variables
    ampl.read('ERMS.mod')    	# Leer modelo
    
    # read data from Data Frames
#    InputClass = AMPLprov_dat()
    [dfT, dfC, dfE, dfT_C, dfT_E] = AMPLdat_inputDF(InputClass)
    # set sizeless param
    # # get parameters from model

	# set values
    try: 
    	# # param sizeless 
        ampl.eval('let kdc  :='+ str(InputClass.kdc)+';')
        ampl.eval('let nab  :='+ str(InputClass.nab)+';')
        ampl.eval('let nin  :='+ str(InputClass.nin)+';')
        ampl.eval('let nsd  :='+ str(InputClass.nsd)+';')
        ampl.eval('let ein  :='+ str(InputClass.ein)+';')
        ampl.eval('let psm  :='+ str(InputClass.psm)+';')
        ampl.eval('let elu  :='+ str(InputClass.elu)+';')
        ampl.eval('let ell  :='+ str(InputClass.ell)+';')
        ampl.eval('let pim  :='+ str(InputClass.pim)+';')
        ampl.eval('let kadn  :='+ str(InputClass.kadn)+';')
        ampl.eval('let katn  :='+ str(InputClass.katn)+';')
        ampl.eval('let ktmv  :='+ str(InputClass.ktmv)+';')
        ampl.eval('let kttn  :='+ str(InputClass.kttn)+';')
        ampl.eval('let kqga  :='+ str(InputClass.kqga)+';')
        ampl.eval('let kqua  :='+ str(InputClass.kqua)+';')
    	# # Dataframe T: assigns Set T and dt, ke, p_pv
        ampl.setData(dfT, 'T')
    	# # Dataframe C: assigns Set C
        ampl.setData(dfC, 'C')
    	# # Dataframe E: assigns Set E
        ampl.setData(dfE, 'E')
    	# # Dataframe T_C: assigns p_l and q_l
        ampl.setData(dfT_C)
    	# # Dataframe T_E: assigns p_e
        ampl.setData(dfT_E)
    except Exception as e:
        print('Error loading imput data to AMPL>' + e)
        raise
    
    # Llamar e modificar opciones do solver
    ampl.option['solver']='cplex'
    ampl.solve()
    
    # calcular tiempo de optimizacion
    opt_t = time.time() - opt_t
    
    # OF = ampl.getObjective('OF')
    class OPTResults:
        opt_time = round(opt_t, 2)
        NT = InputClass.NT
		
        FMT = '%Y-%m-%d-%H:%M'
        FMTS = '%H:%M'
        timestamp_list = pd.date_range(start = datetime.strptime(InputClass.Init_time, FMT),end = datetime.strptime(InputClass.Final_time, FMT),periods = NT).to_pydatetime().tolist()
        timestamp_array = []
        for i in range(NT):
            timestamp_array.append(str(timestamp_list[i]))
        
        P_s = ampl.getData('P_s')
        P_s = P_s.toList()    
    
        Q_s = ampl.getData('Q_s')
        Q_s = Q_s.toList()  
        
        OF = ampl.getObjective("OF")
        OFval = round(OF.value(),3)
        
        opt_conver = ampl.getData("solve_result")
        opt_conv = opt_conver.getRowByIndex(0)[0]
        
    return OPTResults
