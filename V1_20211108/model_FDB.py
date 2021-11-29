
from os import utime
from flask_sqlalchemy import SQLAlchemy
from ConfigAPI.core import app
import enum
from datetime import datetime, time

DB = SQLAlchemy(app)

NameDataBase="FutureDB"

class TypeOfOutput(enum.Enum):
    ERMS = 1
    aFRR = 2
    mFRR = 3
    mCM = 4
    aCM = 5

class TypeOfInput(enum.Enum):
    ERMS = 1
    aFRR = 2
    mFRR = 3
    mCM = 4
    aCM = 5

class classTSO_Forecast_TMD_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'TSO_Forecast_TMD'
    id_TSO = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.Date, nullable=False)
    TMD_Forecast = DB.Column(DB.Float, nullable=False)
     
    def __init__(self, **kwargs):
        super(classTSO_Forecast_TMD_F, self).__init__(**kwargs)

class classDefault_TSO_Forecast_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'Default_TSO_Forecast'
    id_Default_TSO = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.Date, nullable=False)
    PV_forecast_Default = DB.Column(DB.Float, nullable=False)
    TMD_Forecast_Default = DB.Column(DB.Float, nullable=False)
     
    def __init__(self, **kwargs):
        super(classDefault_TSO_Forecast_F, self).__init__(**kwargs)

class classbess_parameter_input_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'bess_parameter_input'
    id_bess = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime, nullable=False,default=DB.func.now())
    P_limit = DB.Column(DB.Float, nullable=False)
    Q_limit = DB.Column(DB.Float, nullable=False)
    injection_eff = DB.Column(DB.Float, nullable=False)
    absortion_eff = DB.Column(DB.Float, nullable=False)
    self_discharge = DB.Column(DB.Float, nullable=False)
    initial_energy = DB.Column(DB.Float, nullable=False)
    energy_upper_limit = DB.Column(DB.Float, nullable=False)
    energy_lower_limit = DB.Column(DB.Float, nullable=False)
     
    def __init__(self, **kwargs):
        super(classbess_parameter_input_F, self).__init__(**kwargs)


class classdemand_charges_1_output_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'demand_charges_1_output'
    id_DE_CH1 = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime, nullable=False,default=DB.func.now())
    P_building_1 = DB.Column(DB.Float, nullable=False)
    P_building_2 = DB.Column(DB.Float, nullable=False)
    tag_process = DB.Column(DB.Integer, nullable=False)
     
    def __init__(self, **kwargs):
        super(classdemand_charges_1_output_F, self).__init__(**kwargs)

  

class classdemand_input_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'demand_input'
    id_demand = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    FK_numberOfset_de=DB.Column(DB.Integer,DB.ForeignKey('numberofset_demande.id_NumberofSet_De'), nullable=False)
    timestamp = DB.Column(DB.DATETIME, nullable=False)
    forecast_P = DB.Column(DB.Float, nullable=False)
    forecast_Q = DB.Column(DB.Float, nullable=False)
    forecast_dev = DB.Column(DB.Float, nullable=False)
   
    def __init__(self, **kwargs):
        super(classdemand_input_F, self).__init__(**kwargs)

             
class classelectricitycharges_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'electricitycharges'
    id_elec = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DATETIME, nullable=False,default=DB.func.now())
    TradersFee = DB.Column(DB.Float, nullable=False)
    Access_DN = DB.Column(DB.Float, nullable=False)
    Access_TN =  DB.Column(DB.Float, nullable=False)
    Trans_via_MV_DN = DB.Column(DB.Float, nullable=False)
    Trans_via_TN =  DB.Column(DB.Float, nullable=False)
    Surchange_for_given_Q = DB.Column(DB.Float, nullable=False)
    Surchange_for_used_Q = DB.Column(DB.Float, nullable=False)

    def __init__(self, **kwargs):
        super(classelectricitycharges_F, self).__init__(**kwargs) 

   

class classev_input_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'ev_input'

    id_EV = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    FK_numberofset_ev=DB.Column(DB.Integer,DB.ForeignKey('numberofset_ev.id_NumberOfSet_EV'),nullable=False)
    timestamp = DB.Column(DB.DATETIME, nullable=False)
    forecast = DB.Column(DB.Float, nullable=False)
    forecast_dev = DB.Column(DB.Float, nullable=False)
   
    def __init__(self, **kwargs):
        super(classev_input_F, self).__init__(**kwargs)

  

class classlec_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'lec'
    id_LEC = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime, nullable=False)
    FK_numberofst_lec=DB.Column(DB.Integer,DB.ForeignKey('numberofst_lec.id_NumberofSet_LEC'),nullable=False)
    FK_id_lec_users = DB.Column(DB.Integer,DB.ForeignKey('lec_users.id_lec_users'),nullable=False)
    forecast = DB.Column(DB.Float, nullable=False)
    parcel_rate = DB.Column(DB.Float, nullable=False)
    
    def __init__(self, **kwargs):
        super(classlec_F, self).__init__(**kwargs)
    
  

class classlec_users_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'lec_users'
    id_lec_users = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    lec_users = DB.Column(DB.String(20),nullable=False)
    lec=DB.relationship('classlec_F',backref='lecUsers')

    def __init__(self, **kwargs):
        super(classlec_users_F, self).__init__(**kwargs)

   

class classnumberofset_demande_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'numberofset_demande'
    id_NumberofSet_De = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    DemantInput= DB.relationship('classdemand_input_F',backref='numberofsetdemande')
    Numberofst_output=DB.relationship('classnumberofst_output_F',backref='numberofsetdemande')
   
    def __init__(self, **kwargs):
        super(classnumberofset_demande_F, self).__init__(**kwargs)

  

class classnumberofset_ev_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'numberofset_ev'
    id_NumberOfSet_EV = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    EvInput=DB.relationship('classev_input_F',backref = 'numberofsetev')
    Numberofst_output=DB.relationship('classnumberofst_output_F',backref='numberofsetEv')

   
    def __init__(self, **kwargs):
        super(classnumberofset_ev_F, self).__init__(**kwargs)

   
class classnumberofset_pv_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'NumberOfSet_PV'
    id_NumberOfSet_PV = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    PvInput=DB.relationship('classpv_input_F',backref = 'NumberOfSetPV')
    Numberofst_output=DB.relationship('classnumberofst_output_F',backref='NumberOfSetPV')
   
    def __init__(self, **kwargs):
        super(classnumberofset_pv_F, self).__init__(**kwargs)
    
  

class classnumberofst_acepted_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'numberofst_acepted'
    id_NumberofSet_Acepted = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    FK_NumberofSet_Output = DB.Column(DB.Integer,DB.ForeignKey('numberofst_output.id_NumberofSet_Output'))
    TypeOfOutput = DB.Column(DB.Enum(TypeOfOutput))
    output_accepted=DB.relationship('classoutput_accepted_F',backref='numberofset')

   
    def __init__(self, **kwargs):
        super(classnumberofst_acepted_F, self).__init__(**kwargs)
    
  

class classnumberofst_input_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'numberofst_input'
    id_NumberofSet_input = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    TypeOfInput = DB.Column(DB.Enum(TypeOfInput))

   # numberofst_output = DB.relationship('classnumberofst_output',backref='numberofstInput',lazy=True)
    typeofinputt = DB.relationship('classtypeofinputt_F',backref='numberofset')
    
   
    def __init__(self, **kwargs):
        super(classnumberofst_input_F, self).__init__(**kwargs)

  

class classnumberofst_lec_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'numberofst_lec'
    id_NumberofSet_LEC = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    Lec=DB.relationship('classlec_F',backref='numberofstlec')
    Numberofst_output=DB.relationship('classnumberofst_output_F',backref='numberofstlec')
   
    def __init__(self, **kwargs):
        super(classnumberofst_lec_F, self).__init__(**kwargs)

class classRel_Opt_NumberOfSetOutput(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'Rel_Opt_NumberOfSetOutput'
    FK_NumberofSet_Output=DB.Column(DB.Integer,DB.ForeignKey('numberofst_output.id_NumberofSet_Output'),primary_key=True)
    FK_optimization_container=DB.Column(DB.Integer,DB.ForeignKey('optimization_container_events.id_OPT'),primary_key=True)


    def __init__(self, **kwargs):
        super(classRel_Opt_NumberOfSetOutput, self).__init__(**kwargs)   

class classnumberofst_output_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'numberofst_output'
    id_NumberofSet_Output = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime, nullable=False,default=DB.func.now())

    NumberofSet_ERMS = DB.Column(DB.Integer)
    NumberofSet_AFrr = DB.Column(DB.Integer)
    NumberofSet_MFrr = DB.Column(DB.Integer)
    NumberofSet_MCM = DB.Column(DB.Integer)
    NumberofSet_ACM = DB.Column(DB.Integer)

    FK_NumberOfSet_pv = DB.Column(DB.Integer, DB.ForeignKey('NumberOfSet_PV.id_NumberOfSet_PV'))
    FK_NumberOfSet_ev = DB.Column(DB.Integer, DB.ForeignKey('numberofset_ev.id_NumberOfSet_EV'))
    FK_NumberOfSet_de = DB.Column(DB.Integer, DB.ForeignKey('numberofset_demande.id_NumberofSet_De'))
    FK_NumberOfSet_Lec = DB.Column(DB.Integer, DB.ForeignKey('numberofst_lec.id_NumberofSet_LEC'))
    TypeOfOutput = DB.Column(DB.Enum(TypeOfOutput))
    
    #optimization_container_events= DB.relationship('classoptimization_container_events_F',backref='numberofstOutput')
    numberofst_acepted=DB.relationship('classnumberofst_acepted_F', backref='numberofset')
    output=DB.relationship('classoutput_F',backref='numberofset')
    
   
    def __init__(self, **kwargs):
        super(classnumberofst_output_F, self).__init__(**kwargs)
    


class classoptimization_container_events_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'optimization_container_events'
    id_OPT = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime, nullable=False, default=DB.func.now())
    convergence = DB.Column(DB.Integer, nullable=False)
    solution_time = DB.Column(DB.Float, nullable=False)
    objective_function = DB.Column(DB.Float, nullable=False)
    number_of_set_output=DB.relationship('classnumberofst_output_F',secondary='Rel_Opt_NumberOfSetOutput',backref='optimizations')
    #FK_NumberofSet_Output = DB.Column(DB.Integer,DB.ForeignKey('numberofst_output.id_NumberofSet_Output'), nullable=False)
   
    def __init__(self, **kwargs):
         super(classoptimization_container_events_F, self).__init__(**kwargs)

    

class classoutput_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'output'
    id_output = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DateTime, nullable=False)
    P_reserve_up = DB.Column(DB.FLOAT)
    P_reserve_down = DB.Column(DB.FLOAT)
    Q_reserve_up = DB.Column(DB.FLOAT)
    Q_reserve_down = DB.Column(DB.FLOAT)
    P_Bid_price_up = DB.Column(DB.FLOAT)
    P_Bid_price_down = DB.Column(DB.FLOAT)
    Q_Bid_price_up = DB.Column(DB.FLOAT)
    Q_Bid_price_down = DB.Column(DB.FLOAT)
    P_Power_schedule = DB.Column(DB.FLOAT)
    Q_Power_schedule = DB.Column(DB.FLOAT)
    FK_NumberOfSet_output=DB.Column(DB.Integer,DB.ForeignKey('numberofst_output.id_NumberofSet_Output'))
   
    def __init__(self, **kwargs):
        super(classoutput_F, self).__init__(**kwargs)

  

class classoutput_accepted_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'output_accepted'
    id_ou_ac = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    FK_numberofst_acepted = DB.Column(DB.Integer,DB.ForeignKey('numberofst_acepted.id_NumberofSet_Acepted'),nullable=False)
    
    timestamp = DB.Column(DB.DATETIME, nullable=False)
    Dispatch_P = DB.Column(DB.FLOAT, nullable=False)
    Dispatch_Q = DB.Column(DB.FLOAT, nullable=False)
    Ofered_P_reserve_up=DB.Column(DB.FLOAT, nullable=False)
    Ofered_P_Power_accepted=DB.Column(DB.FLOAT, nullable=False)
    Ofered_Q_Power_accepted=DB.Column(DB.FLOAT, nullable=False)
    Ofered_P_reserve_down = DB.Column(DB.FLOAT, nullable=False)
    Ofered_Q_reserve_up = DB.Column(DB.FLOAT, nullable=False)
    Ofered_Q_reserve_down = DB.Column(DB.FLOAT, nullable=False)
    Ofered_Price_P_Reserve_up = DB.Column(DB.FLOAT, nullable=False)
    Ofered_Price_Q_Reserve_up = DB.Column(DB.FLOAT, nullable=False)
    Ofered_Price_P_Reserve_down = DB.Column(DB.FLOAT, nullable=False)
    Ofered_Price_Q_Reserve_down = DB.Column(DB.FLOAT, nullable=False)
    Dispatch_P_reserve_up = DB.Column(DB.FLOAT, nullable=False)
    Dispatch_P_reserve_down = DB.Column(DB.FLOAT, nullable=False)
    Dispatch_Q_reserve_up = DB.Column(DB.FLOAT, nullable=False)
    Dispatch_Q_reserve_down = DB.Column(DB.FLOAT, nullable=False)
    Final_Price_P_Reserve_up = DB.Column(DB.FLOAT, nullable=False)
    Final_Price_P_Reserve_down = DB.Column(DB.FLOAT, nullable=False)
    Final_Price_Q_Reserve_up = DB.Column(DB.FLOAT, nullable=False)
    Final_Price_Q_Reserve_down = DB.Column(DB.FLOAT, nullable=False)
    status=DB.Column(DB.Boolean, nullable=False)
     
    def __init__(self, **kwargs):
        super(classoutput_accepted_F, self).__init__(**kwargs)

  

class classpv_input_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'pv_input'
    id_PV = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    FK_NumberOfSet_PV= DB.Column(DB.Integer,DB.ForeignKey('NumberOfSet_PV.id_NumberOfSet_PV'))
    timestamp = DB.Column(DB.DATETIME, nullable=False)
    forecast = DB.Column(DB.Float, nullable=False)
    forecast_dev = DB.Column(DB.Float, nullable=False)
   
    def __init__(self, **kwargs):
        super(classpv_input_F, self).__init__(**kwargs)

   
class classtypeofinputt_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'typeofinput'
    id_INPUT = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    timestamp = DB.Column(DB.DATETIME, nullable=False)
    forecast_P_price_up = DB.Column(DB.FLOAT, nullable=False)
    forecast_P_price_down = DB.Column(DB.FLOAT, nullable=False)
    forecast_Q_price_up = DB.Column(DB.FLOAT, nullable=False)
    forecast_Q_price_down = DB.Column(DB.FLOAT, nullable=False)
    P_forecast_price_dev= DB.Column(DB.FLOAT, nullable=False)
    Q_forecast_price_dev= DB.Column(DB.FLOAT, nullable=False)
    Requirement_P_reserve_up = DB.Column(DB.FLOAT, nullable=False)
    Requirement_P_reserve_down = DB.Column(DB.FLOAT, nullable=False)
    Requirement_Q_reserve_up = DB.Column(DB.FLOAT, nullable=False)
    Requirement_Q_reserve_down = DB.Column(DB.FLOAT, nullable=False)
    Max_limit = DB.Column(DB.FLOAT, nullable=False)
    Min_limit = DB.Column(DB.FLOAT, nullable=False)
    P_forecast_price = DB.Column(DB.FLOAT, nullable=False)
    Q_forecast_price = DB.Column(DB.FLOAT, nullable=False)
    FK_NumberOfSet_input = DB.Column(DB.Integer,DB.ForeignKey('numberofst_input.id_NumberofSet_input'), nullable=False)
    
    
    def __init__(self, **kwargs):
        super(classtypeofinputt_F, self).__init__(**kwargs)


class classmarketStatus_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'market_status'
    id_MA = DB.Column(DB.Integer, primary_key=True, autoincrement = True)
    service = DB.Column(DB.Enum(TypeOfInput), nullable=False)
    Submitted_Bid = DB.Column(DB.Boolean, nullable=False)
    Market_Status = DB.Column(DB.String(20), nullable=False)
    Opening_Time = DB.Column(DB.String(20), nullable=False)
    Closing_Time = DB.Column(DB.String(20), nullable=False)
    Requirement_Received = DB.Column(DB.Boolean, nullable=False)
    Dispatch_Received= DB.Column(DB.Boolean,nullable=False)

    def __init__(self, **kwargs):
        super(classmarketStatus_F, self).__init__(**kwargs)

   

class classdefault_input_F(DB.Model):
    __bind_key__ = NameDataBase
    __tablename__ = 'default_input'
    id_default_input= DB.Column(DB.Integer,primary_key=True,autoincrement=True)
    timestamp= DB.Column(DB.DateTime,nullable = False)
    forecast_P_price_up=DB.Column(DB.Float(),nullable=False)
    forecast_P_price_down=DB.Column(DB.Float(),nullable=False)
    forecast_Q_price_up=DB.Column(DB.Float(),nullable=False)
    forecast_Q_price_down=DB.Column(DB.Float(),nullable=False)
    Requirement_P_reserve_up=DB.Column(DB.Float(),nullable=False)
    Requirement_P_reserve_down=DB.Column(DB.Float(),nullable=False)
    Requirement_Q_reserve_up=DB.Column(DB.Float(),nullable=False)
    Requirement_Q_reserve_down=DB.Column(DB.Float(),nullable=False)
    P_forecasted_price=DB.Column(DB.Float(),nullable=False)
    Q_forecasted_price=DB.Column(DB.Float(),nullable=False)
    Max_limit=DB.Column(DB.Float(),nullable=False)
    Min_limit=DB.Column(DB.Float(),nullable=False)
    TypeOfInput=DB.Column(DB.Enum(TypeOfInput))

    def __init__(self, **kwargs):
     super(classdefault_input_F, self).__init__(**kwargs)

  

if __name__ == "__main__":
    DB.create_all(bind=NameDataBase)


