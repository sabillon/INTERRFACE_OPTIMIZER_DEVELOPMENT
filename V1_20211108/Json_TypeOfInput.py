
### librerias en github 
import model_FDB
from model_FDB import  DB as DB_F
from CollectionOfQueries import QS




## read relation table 
Json={
    "ERMS_o": 1,
    "mCM_o": 18,
    "mFRR_o": 12,
    "aFRR_o": 7,
    "aCM_o": 22,
}
table=model_FDB.classnumberofst_input_F
secTable=model_FDB.classtypeofinputt_F
for k in Json.keys():
    crit=model_FDB.classnumberofst_input_F.id_NumberofSet_input == Json[k]
    query = QS.read_relationTable(DB_F,table,crit,secTable)                  

    if isinstance(query,list):
        ## obtenemos una lista de objetos relacionados con la query obtenida
        for listobj in query: 
            listobj=list(listobj)
            if len(listobj) != 0:
                # obtenemos los valores de cada objeto
                for obj in listobj:
                    for key,value in obj.__dict__.items():
                        if key != "_sa_instance_state":
                            print("\nkey: "+str(key),"value: "+str(value))
                            ## Carlos con estos valores creamos un json
                
    else:
        print(query)

#######