# from ConfigAPI.core import app, DB

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask import Flask
import requests
import enum



app_settings = os.getenv(
    'APP_SETTINGS',
    'config.DevelopmentConfig'
)
app = Flask(__name__)
app.config.from_object(app_settings)
DB = SQLAlchemy(app)


class TypeOfInput(enum.Enum):
    ERMS = 1
    AFrr = 2
    MFrr = 3
    MANUAL_CM = 4
    Automatic_CM = 5



class classDemand_input(DB.Model):
    __tablename__ = 'Demand_input'
    id_Demand = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime)
    P_forecast = DB.Column(DB.Float)
    Q_forecast = DB.Column(DB.Float)
    NumberOfSet_de = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_de.NumberOfSet_de'))
     
    def __init__(self, id_Demand=None, timestamp=None, forecast=None, NumberOfSet_de=None):
        self.id_Demand = id_Demand
        self.timestamp = timestamp
        self.forecast = forecast
        self.NumberOfSet_de = NumberOfSet_de
                 
        
class classEV_input(DB.Model):
    __tablename__ = 'EV_input'
    id_ev = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime)
    forecast = DB.Column(DB.Float)
    NumberOfSet_ev = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_ev.NumberOfSet_ev'))
     
    def __init__(self, id_ev=None, timestamp=None, forecast=None, NumberOfSet_ev=None):
        self.id_ev = id_ev
        self.timestamp = timestamp
        self.forecast = forecast
        self.NumberOfSet_ev = NumberOfSet_ev
                 
        
class classLEC(DB.Model):
    __tablename__ = 'LEC'
    id_LEC = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime)
    forecast = DB.Column(DB.Float)
    parcel_rate = DB.Column(DB.Float)
    NumberOfSet_LEC = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_LEC.NumberOfSet_LEC'))
     
    def __init__(self, id_LEC=None, timestamp=None, forecast=None, parcel_rate=None, NumberOfSet_LEC=None):
        self.id_LEC = id_LEC
        self.timestamp = timestamp
        self.forecast = forecast
        self.parcel_rate = parcel_rate
        self.NumberOfSet_LEC = NumberOfSet_LEC
                 
        
class classNumberOfSet_de(DB.Model):
    __tablename__ = 'NumberOfSet_de'
    NumberOfSet_de = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    user_asset_id = DB.Column(DB.Integer)
     
    def __init__(self, NumberOfSet_de=None, user_asset_id=None):
        self.NumberOfSet_de = NumberOfSet_de
        self.user_asset_id = user_asset_id
                 
        
class classNumberOfSet_ev(DB.Model):
    __tablename__ = 'NumberOfSet_ev'
    NumberOfSet_ev = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    user_asset_id = DB.Column(DB.Integer)
     
    def __init__(self, NumberOfSet_ev=None, user_asset_id=None):
        self.NumberOfSet_ev = NumberOfSet_ev
        self.user_asset_id = user_asset_id
                 
        
class classNumberOfSet_input(DB.Model):
    __tablename__ = 'NumberOfSet_input'
    NumberOfSet_input = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    user_asset_id = DB.Column(DB.Integer)
    TypeOfInput = DB.Column(DB.Enum(TypeOfInput))
     
    def __init__(self, NumberOfSet_input=None, user_asset_id=None, TypeOfInput=None):
        self.NumberOfSet_input = NumberOfSet_input
        self.user_asset_id = user_asset_id
        self.TypeOfInput = TypeOfInput
                 
        
class classNumberOfSet_LEC(DB.Model):
    __tablename__ = 'NumberOfSet_LEC'
    NumberOfSet_LEC = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    user_asset_id = DB.Column(DB.Integer)
    ID_meter = DB.Column(DB.Integer)
     
    def __init__(self, NumberOfSet_LEC=None, user_asset_id=None, ID_meter=None):
        self.NumberOfSet_LEC = NumberOfSet_LEC
        self.user_asset_id = user_asset_id
        self.ID_meter = ID_meter
                 
        

                 
        
class classNumberOfSet_pv(DB.Model):
    __tablename__ = 'NumberOfSet_pv'
    NumberOfSet_pv = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    user_asset_id = DB.Column(DB.Integer)
     
    def __init__(self, NumberOfSet_pv=None, user_asset_id=None):
        self.NumberOfSet_pv = NumberOfSet_pv
        self.user_asset_id = user_asset_id
                 
        
class classOUTPUT(DB.Model):
    __tablename__ = 'OUTPUT'
    ID_INPUT = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime)
    P_reserve_up = DB.Column(DB.Float)
    Q_reserve_up = DB.Column(DB.Float)
    P_reserve_down = DB.Column(DB.Float)
    Q_reserve_down = DB.Column(DB.Float)
    P_Bid_price_up = DB.Column(DB.Float)
    P_Bid_price_down = DB.Column(DB.Float)
    Q_Bid_price_up = DB.Column(DB.Float)
    Q_Bid_price_down = DB.Column(DB.Float)
    P_Power_schedule = DB.Column(DB.Float)
    Q_Power_schedule = DB.Column(DB.Float)
    NumberofSet_Output = DB.Column(DB.Float)
    # NumberofSet_Output = DB.Column(DB.Float, DB.ForeignKey('NumberOfSet_output.NumberOfSet_output'))
     
    def __init__(self, ID_INPUT=None, timestamp=None, P_reserve_up=None, Q_reserve_up=None, P_reserve_down=None, Q_reserve_down=None, P_Bid_price_up=None, P_Bid_price_down=None, Q_Bid_price_up=None, Q_Bid_price_down=None, P_Power_schedule=None, Q_Power_schedule=None, NumberofSet_Output=None):
        self.ID_INPUT = ID_INPUT
        self.timestamp = timestamp
        self.P_reserve_up = P_reserve_up
        self.Q_reserve_up = Q_reserve_up
        self.P_reserve_down = P_reserve_down
        self.Q_reserve_down = Q_reserve_down
        self.P_Bid_price_up = P_Bid_price_up
        self.P_Bid_price_down = P_Bid_price_down
        self.Q_Bid_price_up = Q_Bid_price_up
        self.Q_Bid_price_down = Q_Bid_price_down
        self.P_Power_schedule = P_Power_schedule
        self.Q_Power_schedule = Q_Power_schedule
        self.NumberofSet_Output = NumberofSet_Output
                 
class classNumberOfSet_output(DB.Model):
    __tablename__ = 'NumberOfSet_output'
    NumberOfSet_output = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    NumberOfSet_ERMS = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_input.NumberOfSet_input'), nullable=True)
    NumberOfSet_AFrr = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_input.NumberOfSet_input'), nullable=True)
    NumberOfSet_MFrr = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_input.NumberOfSet_input'), nullable=True)
    NumberOfSet_MCM = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_input.NumberOfSet_input'), nullable=True)
    NumberOfSet_ACM = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_input.NumberOfSet_input'), nullable=True)
    NumberOfSet_pv = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_pv.NumberOfSet_pv'), nullable=True)
    NumberOfSet_ev = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_ev.NumberOfSet_ev'), nullable=True)
    NumberOfSet_de = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_de.NumberOfSet_de'), nullable=True)
    NumberOfSet_LEC = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_LEC.NumberOfSet_LEC'), nullable=True)
    TypeOfInput = DB.Column(DB.Enum(TypeOfInput))
     
    def __init__(self, NumberOfSet_output=None, NumberOfSet_ERMS=None, NumberOfSet_AFrr=None, NumberOfSet_MFrr=None, NumberOfSet_MCM=None, NumberOfSet_ACM=None, NumberOfSet_pv=None, NumberOfSet_ev=None, NumberOfSet_de=None, NumberOfSet_LEC=None, TypeOfInput=None):
        self.NumberOfSet_output = NumberOfSet_output
        self.NumberOfSet_ERMS = NumberOfSet_ERMS
        self.NumberOfSet_AFrr = NumberOfSet_AFrr
        self.NumberOfSet_MFrr = NumberOfSet_MFrr
        self.NumberOfSet_MCM = NumberOfSet_MCM
        self.NumberOfSet_ACM = NumberOfSet_ACM
        self.NumberOfSet_pv = NumberOfSet_pv
        self.NumberOfSet_ev = NumberOfSet_ev
        self.NumberOfSet_de = NumberOfSet_de
        self.NumberOfSet_LEC = NumberOfSet_LEC
        self.TypeOfInput = TypeOfInput      
        

class classPV_input(DB.Model):
    __tablename__ = 'PV_input'
    id_pv = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime)
    forecast = DB.Column(DB.Float)
    NumberOfSet_pv = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_pv.NumberOfSet_pv'))
     
    def __init__(self, id_pv=None, timestamp=None, forecast=None, NumberOfSet_pv=None):
        self.id_pv = id_pv
        self.timestamp = timestamp
        self.forecast = forecast
        self.NumberOfSet_pv = NumberOfSet_pv
                 
        
class classTypeOfINPUT(DB.Model):
    __tablename__ = 'TypeOfINPUT'
    ID_INPUT = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime)
    forecast_P_price_up = DB.Column(DB.Float)
    forecast_P_price_down = DB.Column(DB.Float)
    forecast_Q_price_up = DB.Column(DB.Float)
    forecast_Q_price_down = DB.Column(DB.Float)
    Requirement_P_reserve_up = DB.Column(DB.Float)
    Requierement_P_reserve_down = DB.Column(DB.Float)
    Requirement_Q_reserve_up = DB.Column(DB.Float)
    Requierement_Q_reserve_down = DB.Column(DB.Float)
    Max_limit = DB.Column(DB.Float)
    Min_limit = DB.Column(DB.Float)
    P_forecasted_price = DB.Column(DB.Float)
    Q_forecasted_price = DB.Column(DB.Float)
    NumberOfSet_input = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_input.NumberOfSet_input'))
     
    def __init__(self, ID_INPUT=None, timestamp=None, forecast_P_price_up=None, forecast_P_price_down=None, forecast_Q_price_up=None, forecast_Q_price_down=None, Requirement_P_reserve_up=None, Requierement_P_reserve_down=None, Requirement_Q_reserve_up=None, Requierement_Q_reserve_down=None, Max_limit=None, Min_limit=None, P_forecasted_price=None, Q_forecasted_price=None, NumberOfSet_input=None):
        self.ID_INPUT = ID_INPUT
        self.timestamp = timestamp
        self.forecast_P_price_up = forecast_P_price_up
        self.forecast_P_price_down = forecast_P_price_down
        self.forecast_Q_price_up = forecast_Q_price_up
        self.forecast_Q_price_down = forecast_Q_price_down
        self.Requirement_P_reserve_up = Requirement_P_reserve_up
        self.Requierement_P_reserve_down = Requierement_P_reserve_down
        self.Requirement_Q_reserve_up = Requirement_Q_reserve_up
        self.Requierement_Q_reserve_down = Requierement_Q_reserve_down
        self.Max_limit = Max_limit
        self.Min_limit = Min_limit
        self.P_forecasted_price = P_forecasted_price
        self.Q_forecasted_price = Q_forecasted_price
        self.NumberOfSet_input = NumberOfSet_input
                 
    
DB.create_all()

#Insertar una fila

#obj = classNumberOfSet_pv(user_asset_id= 2)
#DB.session.add(obj)

# Subirla a la DB
#DB.session.commit()

#Select la primera fila ordenando por el number of set en orden descendente
#obj = classNumberOfSet_pv.query.order_by(classNumberOfSet_pv.NumberOfSet_pv.desc()).first()
#print(obj[0].user_asset_id)

# Crear 24 puntos con valores de hoy saltados cada hora
#for i in range(24):
#    obj_pv= classPV_input(timestamp= datetime.datetime.today()+datetime.timedelta(hours=i),forecast= i*2,NumberOfSet_pv= obj[0].user_asset_id)
#    DB.session.add(obj_pv)
## Subirlos a las DB
#DB.session.commit()

# Leer los 24 puntos anteriores
#Set_of_obj = classPV_input.query.filter(classPV_input.NumberOfSet_pv==3).order_by(classPV_input.timestamp.asc()).all()
#
#info_serial = []
#for object in Set_of_obj:
#    info_serial.append([object.timestamp.strftime("%m/%d/%Y, %H:%M:%S"),object.forecast])
##
##print(info_serial)
#    
#    
#obj=classNumberOfSet_output(NumberOfSet_ERMS=json_out['aFRR_o'], NumberOfSet_AFrr=None, NumberOfSet_MFrr=None, NumberOfSet_MCM=None, NumberOfSet_ACM=None, NumberOfSet_pv=None, NumberOfSet_ev=None, NumberOfSet_de=None, NumberOfSet_LEC=None, TypeOfInput="ERMS")
#DB.session.add(obj)
#for i in range(24):
#    obj2=classOUTPUT( timestamp=None, P_reserve_up=None, Q_reserve_up=None, P_reserve_down=None, Q_reserve_down=None, P_Bid_price_up=None, P_Bid_price_down=None, Q_Bid_price_up=None, Q_Bid_price_down=None, P_Power_schedule=None, Q_Power_schedule=None, NumberofSet_Output=obj.NumberOfSet_output)
#    DB.session.add(obj)
#DB.session.commit()

def AMPL_dat_DBs(json_in):
    # Consult DBs
    ip_EM="127.0.0.1:5000"
    # ip_EM="172.16.239.2:5000"
    response = requests.get("http://"+ip_EM+"/DB_Autoritzation",json={"activity":'Read', "DB":'FDB'})
    if response.json()["Acces"] == 'True' :
        print('\n\n FDB access granted \n')    
        # T
        FMT = '%Y-%m-%d-%H:%M'
        FMTS = '%H:%M'
        time_diff = datetime.strptime(json_in['Final_time'], FMT) - datetime.strptime(json_in['Init_time'], FMT)
        time_step = datetime.strptime(json_in['Time_step'], FMTS)
        time_step_sec = time_step.hour * 3600 + time_step.minute * 60
        Number_of_intervals = (time_diff.days*24*3600 + time_diff.seconds)/time_step_sec + 1
        # PV
        Set_of_obj_p_pv = classPV_input.query.filter(classPV_input.NumberOfSet_pv==json_in['PV_i']).order_by(classPV_input.timestamp.asc()).all()
        # Demand 
        Set_of_obj_p_l = classDemand_input.query.filter(classDemand_input.NumberOfSet_de==json_in['Dem_i']).order_by(classDemand_input.timestamp.asc()).all()
        # EV
        Set_of_obj_p_e = classEV_input.query.filter(classEV_input.NumberOfSet_ev==json_in['EV_i']).order_by(classEV_input.timestamp.asc()).all()
        # ke
        Set_of_obj_ke = classTypeOfINPUT.query.filter(classTypeOfINPUT.NumberOfSet_input==json_in['ERMS_i']).order_by(classTypeOfINPUT.timestamp.asc()).all()

        
        class AMPLinput:
            # Creation Flag
            create = 1
            Init_time = json_in["Init_time"]
            Final_time = json_in["Final_time"]
            
            # T
            NT = Number_of_intervals
            Times = range(1, int(Number_of_intervals))
            dt = [time_step_sec / 60] * int(Number_of_intervals)
            # Consumers
            Consu = [1]
            # EVs
            EVs = [1]
            # PV
            p_pv = []
            for object in Set_of_obj_p_pv:
                p_pv.append([object.forecast])  
            # Demand
            p_l = []
            q_l = []
            for object in Set_of_obj_p_l:
                p_l.append([object.P_forecast])  
                q_l.append([object.Q_forecast])
            # EVs
            p_e = []
            for object in Set_of_obj_p_e:
                p_e.append([object.forecast])    
            # ke
            ke = []
            keq = []
            for object in Set_of_obj_ke:
                ke.append([object.P_forecasted_price])          
                keq.append([object.Q_forecasted_price])          
            # param
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
            print('\n\n FDB read succesfully \n')    
    else :
        print('Unable to access DBs for reading input')
        class AMPLinput:
            # Creation Flag
            create = 0
    return AMPLinput

def AMPL_res_DBs(json_out, OPTResults):# Save DBs
    ip_EM="172.16.239.2:5000"
    response = requests.get("http://"+ip_EM+"/DB_Autoritzation",json={"activity":'Write', "DB":'FDB'})
    if response.json()["Acces"] == 'True' :
        print('\n\n FDB access granted \n')    
        obj = classNumberOfSet_output(NumberOfSet_ERMS=None, NumberOfSet_AFrr=json_out["aFRR_o"], NumberOfSet_MFrr=json_out["mFRR_o"], NumberOfSet_MCM=json_out["mCM_o"], NumberOfSet_ACM=json_out["aCM_o"], NumberOfSet_pv=None, NumberOfSet_ev=None, NumberOfSet_de=None, NumberOfSet_LEC=None, TypeOfInput="ERMS")
        DB.session.add(obj)
        DB.session.commit()
        for i in range(OPTResults.NT):
            obj2=classOUTPUT(timestamp=OPTResults.timestamp_array[i], P_reserve_up=None, Q_reserve_up=None, P_reserve_down=None, Q_reserve_down=None, P_Bid_price_up=None, P_Bid_price_down=None, Q_Bid_price_up=None, Q_Bid_price_down=None, P_Power_schedule=OPTResults.P_s[i][1], Q_Power_schedule=OPTResults.Q_s[i][1], NumberofSet_Output=obj.NumberOfSet_output)
            DB.session.add(obj2)
        DB.session.commit()
        print('\n\n FDB read succesfully \n')    
    else :
        print('Unable to access DBs for writing results')