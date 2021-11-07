# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:43:30 2021

@author: baltas
modificated: Juan Benitez
"""
import numpy as np
import datetime
from sqlalchemy import and_


class QS:
    def __init__(self):
        """ The QS class collects all the queries used to interact with the tables
        in a database, i.e. reading, writing, filtering and so on. """
        pass
    
    @staticmethod
    def read_filter(db,table, criterion, ordered=None):
        """
        The filter method of the QS class is a wrapper of the 
        sqlalchemy.orm.Query.filter method. This method applies the
        given filtering criterion to a table ordering the results according to
        their timestamp.

        Parameters
        ----------
        table : flask_sqlalchemy.model.DefaultMeta
            The table of a database.
        criterion : TYPE
            The criterion for filtering the entries in the table.
        ordered : TYPE, optional
            Return the entires ordered according the definition in the variable.

        Returns
        -------
        TYPE
            The filter entries from the table.

        """
        try:
        # Get NumberOfSet_XX attribute for table
        # NOS = [i for i in table.__dict__.keys() if 'NumberOfSet' in i][0]
            if ordered is not None:    
                objs= table.query.filter(criterion).order_by(ordered).all()
            
            objs = table.query.filter(criterion).all()

        
            return objs

        except Exception as e:
            db.session.rollback()
            return e.args
    
    @staticmethod
    def read(db,table):
        """
        Read all Table

        Parameters
        ----------
        table : flask_sqlalchemy.model.DefaultMeta
            The table of a database.

        Returns
        -------
        TYPE
            The filter entries from the table.

        """

        try:
            objs = table.query.all()

            return objs

        except Exception as e:
            db.session.rollback()
            return e.args
    
    @staticmethod
    def write(db, table, Dictionary = None):
        """
        The method writes to a database table by using a dictionary where the 
        keys correspond to the attributes of the table and the items to the 
        values of these attributes. The items can be more than one for this 
        reason the items need to be store in an iteratable such as a list 
        even if only one item per key is passed.

        Parameters
        ----------
        db : flask_sqlalchemy.SQLAlchemy
            Configuration of a DB in SQLAlchemy

        table : flask_sqlalchemy.model.DefaultMeta
            The table of a database.
        Dictionary : dict
            The dictionary containing the attributes of the table (as keys) and
            the values for these attributes.
            Warning: the values of the dictionary must be a array.

        Returns
        -------
        TYPE
            return a object if the operation is succeful or print the exeption if an error
            has occured.

        """
        
        
        """""
        # assign the table into a new variable
        obj = table
        # Get all values of the dicitionary and put them into an array
        vals = np.array(list(Dictionary.values()))
        # Get the keys of the dictionary
        keys = list(Dictionary.keys())
        # Parse each row and col of the vals array, where rows=keys, cols=results
        rows, cols = vals.shape
        for c in range(cols):
            for r in range(rows):
                # set the attributes obj.key = val
                setattr(obj, keys[r], vals[r,c])
                db.session.add(obj)
        """
        ## if not get any dictionary then the id will be incremented and  will add null values
        if Dictionary is None:
            x=table()
            db.session.add(x)
            
        else:
            x=[]
            vals = np.array(list(Dictionary.values()))
            rows, cols = vals.shape
            for c in range(cols):
                dic={}
                for key, values in Dictionary.items():
                    if isinstance(values,list):
                        dic[key]=values[c]
                    else: 
                        return "the values of the dictionay not are type list"
                
                x.append(table(**dic))
                db.session.add(x[c])
            

        try: 
            db.session.commit()
            return x
        except Exception as e:
            db.session.rollback()
            return e.args

    @staticmethod
    def update_a_row(db,table, Dictionary, criteria):
        """"
        The method update the information in one row in the database table 
        by using a dictionary where the keys correspond to the attributes
        of the table and the items to the values of these attributes.
        Only one row at a time is updated

        Parameters
        ----------
        table : flask_sqlalchemy.model.DefaultMeta
            The table of a database.
        Dictionary : dict
            The dictionary containing the attributes of the table (as keys) and
            the values for these attributes.
        criterion : TYPE
            The criterion for finding the row to update in the table.

        Returns
        -------
        None
        """""""""""
        
        # assign the table into a new variable
        obj = QS.read_filter(db,table, criteria)[0]
        # Get all values of the dicitionary and put them into an array
        vals = np.array(list(Dictionary.values()))
        # Get the keys of the dictionary
        keys = list(Dictionary.keys())
        # Parse each row and col of the vals array, where rows=keys, cols=results
        rows, cols = vals.shape
        for c in range(cols):
            for r in range(rows):
                # set the attributes obj.key = val
                setattr(obj, keys[r], vals[r,c]) 
        
    @staticmethod
    def update_finish(db):
        """
        This method close the update of row by row to save it in the datbase.

        Parameters
        ----------
        db : flask_sqlalchemy.SQLAlchemy
            Configuration of a DB in SQLAlchemy

        Returns
        -------
        TYPE
            The object that was updated to the database or False if an error
            has occured.

        """
        try:
            print(type(db)) 
            db.session.commit()
            return True
        except:  # Dont now the exact code error this will throw in case add and commit fail
            return False

    @staticmethod    
    def concat(inputs, join_key='-'):
        if isinstance(inputs, list):
            x = [str(i) for i in inputs]
            return join_key.join(x)


    @staticmethod
    def update_multiple_row(db,table, Dictionary, criteria, ordered= None):
        """
        The method update the information in a group of rows in the database table 
        by using a dictionary where the keys correspond to the attributes
        of the table and the items to the values of these attributes.
        Multiple rows can be updated but the order in the Dictionary have to follow the order in ordered.
        Parameters
        ----------
        db : flask_sqlalchemy.SQLAlchemy
            Configuration of a DB in SQLAlchemy  
        table : flask_sqlalchemy.model.DefaultMeta
            The table of a database.
        Dictionary : dict
            The dictionary containing the attributes of the table (as keys) and
            the values for these attributes.
        criterion : TYPE
            The criterion for finding the rows to update in the table.
        ordered : TYPE, optional
            Order To find the rows in the database that have to be the same as they are in the Dictionary.
        Returns
        -------
        TYPE
            True if the operation is succesful or print the exeption if an error
            has occured.
        """
        objs = QS.read_filter(db,table, criteria,ordered=ordered)
        i = 0
        for obj in objs:
            rowDictionary = {}
            for key in Dictionary.keys():
                rowDictionary[key] = Dictionary[key][i]
            for key, value in rowDictionary.items():
                setattr(obj, key, value)
            i += 1
        
        try: 
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e.args

    

    @staticmethod
    def read_relationTable(db,table,criteria,SecondTable):
        """"
        This method get the value of the relation table according to the criterion searched in the other table 

        Parameters
        ----------
        db : flask_sqlalchemy.SQLAlchemy
            Configuration of a DB in SQLAlchemy

        table : flask_sqlalchemy.model.DefaultMeta
            The table of a database.
       
        criterion : TYPE
            The criterion for finding the row  in the table.

        SecondTable: flask_sqlalchemy.model.DefaultMeta
            The relation table  with the other table of a database.

        Returns
        -------
        Return list the object from the relation table or None if the search criteria is not found 
        """""""""""

        objs=QS.read_filter(db,table,criteria)
        
        if objs != None:
            try:
                SecObjs=[]
                for obj in objs:
                    q=SecondTable.query.with_parent(obj)
                    SecObjs.append(q)
                
                return SecObjs


            except Exception as e:
                db.session.rollback()
                return e.args
                

        else:
            return None
        
    
    @staticmethod
    def delete_filter(db,table,criteria,ordered=None):
        """"
        This method delete the rows according to the filter entries

        Parameters
        ----------
        db : flask_sqlalchemy.SQLAlchemy
            Configuration of a DB in SQLAlchemy
        table : flask_sqlalchemy.model.DefaultMeta
            The table of a database.
        criterion : TYPE
            The criterion for filtering the entries in the table.
        ordered : TYPE, optional
            Return the entires ordered according the definition in the variable.


        Returns
        -------
        true  if the process is succesful or the exeption print if an error
            has occured.
        """""""""""

        # db.query.filter(criteria).delete()
        # db.session.commit()


        objs=QS.read_filter(db,table,criteria,ordered)

        for obj in objs:
            db.session.delete(obj)
        
        try:
            db.session.commit()
            return True
        except Exception as e:
                db.session.rollback()
                return e.args

    @staticmethod
    def delete_object(db,objs):
        """"
        This method delete the rows according to the object entries

        Parameters
        ----------
        db : flask_sqlalchemy.SQLAlchemy
            Configuration of a DB in SQLAlchemy
        object : object obtains of the previus searching
       

        Returns
        -------
        true  if the process is succesful or the exeption print if an error
            has occured.
        """""""""""
        for obj in objs:
            db.session.delete(obj)
   
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e.args


    @staticmethod
    def store_RTtoPAST(db_past,db_RT,tableRT,Past_table):

        """"
        This method get the table values the last day  of DB RT  and stored the values concatenated in table PastDB 

        Parameters
        ----------
        db_past : flask_sqlalchemy.SQLAlchemy
            Configuration of a DB in SQLAlchemy
        tableRT : flask_sqlalchemy.model.DefaultMeta
            The table of a database.
        Past_table : flask_sqlalchemy.model.DefaultMeta
            The table of a database.

        EXAMPLE:    db_past: DB_P
                    tableRT: classoutput_R
                    Past_table: class_output_P
                    outputRT: true

        Returns
        -------
        true if the process is succesful or the exeption print if an error
            has occured.
        """""""""""

        #Conseguimos el objeto datetime de hoy a las 0:00 y un time delta de mañana
        now = datetime.datetime.now()
        today = datetime.datetime(year= now.year,month= now.month,day= now.day)
        deltatime_1_day = datetime.timedelta(days=1)
        lastday= today - deltatime_1_day

       
        #buscamos en la base de datos output las filas con el tiempo de ayer y anteayer con el servicio que buscamos, ordenado por timestamp. Esto nos devolvera una lista de objetos donde los atributos de estos objetos seran el valor de cada fila.

        condition = and_(tableRT.timestamp>=lastday ,tableRT.timestamp<today)
        orderer =  tableRT.timestamp.asc()

        objs= QS.read_filter(db_RT,tableRT,condition,orderer)

        if len(objs) == 0: 
            return False
        
        #creamos una lista con los atributos de la tabla de pasado
        GetColumnPast=[ column.key for column in Past_table.__table__.columns]
            

        #### if table is output_RT we concat order by typeOfOutput
        if tableRT.__table__.name == 'output':

            nestedDict={}
            for obj in objs:
                typ= obj.TypeOfOutput.name
                for key_obj,value_obj in obj.__dict__.items():
                    if key_obj != "_sa_instance_state" and key_obj!= "timestamp" and key_obj!= "TypeOfOutput":
                        if typ in nestedDict:
                            if key_obj in nestedDict[typ]:
                                str_value=str(nestedDict[typ][key_obj])
                                nestedDict[typ][key_obj] = str_value + "," + str(value_obj)
                            else:
                                nestedDict[typ][key_obj] = str(value_obj)
                        else:
                            nestedDict[typ]={key_obj:str(value_obj)}


            for id_nestedDict, keys_nestedDict in nestedDict.items():
                newdic={}
                newdic["TypeOfOutput"]=id_nestedDict
                newdic["timestamp"]=lastday
                for key_nested,value_nested in keys_nestedDict.items():
                    if "id_" in key_nested:
                        pass
                    else:
                        if key_nested in GetColumnPast:
                            newdic[key_nested]=value_nested
                    
                
                #almacenamos los valores contenido en el dictionary
                x=Past_table(**newdic)        
                db_past.session.add(x)



    
        else:
            #### creamos disctionary con las key del obj obtenido
            array={}
            for key in objs[0].__dict__.keys():
                        
                array[key]=""      
            

            ####concatenamos los valores de cada atributo en un array
            for obj in objs:        
            
                for key,value in obj.__dict__.items():
                    if key != "_sa_instance_state" and key!= "timestamp":
                        
                        val=str(array[key])
                        if val != "":
                            array[key] = val +"," + str(value)
                        else:
                            array[key]=str(value)

         

            # comparamos los atributos de la tabla de pasado con los de la tabla RT or Fut,
            # creando un diccionario solo de los atributos que coincidan de la tabla de pasado
            dict={}
            for key, value in array.items(): 
                if key in GetColumnPast:
                    if "id_" in key:
                        pass
                    else:
                        if key != "timestamp":
                            dict[key]=value
                        else:
                            dict[key]=lastday
                    

            #almacenamos los valores contenido en el dictionary
            x=Past_table(**dict)        
            db_past.session.add(x)



        try: 
            db_past.session.commit() # cerramos sesion y enviamos todo.
            QS.delete_object(db_RT,objs)
            return True
        except Exception as e:
            db_past.session.rollback()
            return e.args

    
    @staticmethod
    def store_FUTtoPAST(db_past,db_F,tableFut,Past_table):

        """"
        This method get the values the next day  of DB_Fut and its relation table and stored in table PastDB 

        Parameters
        ----------
        db_past : flask_sqlalchemy.SQLAlchemy
            Configuration of a DB in SQLAlchemy
        table : flask_sqlalchemy.model.DefaultMeta
            The table of database.
        Past_table : flask_sqlalchemy.model.DefaultMeta
            The table of Past database

        EXAMPLE:    db_past: DB_P
                    table: classoutput_F
                    Past_table: class_OUTPUT_P


        Returns
        -------
        if the process is succesful return a list with true and the objs or the exeption print if an error
            has occured.
        """""""""""

        #Conseguimos el objeto datetime de hoy a las 0:00 y un time delta de mañana
        now = datetime.datetime.now()
        today = datetime.datetime(year= now.year,month= now.month,day= now.day)
        deltatime_1_day = datetime.timedelta(days=1)
        nextday = today + deltatime_1_day
       
        #buscamos en la base de datos output las filas con el tiempo de ayer y anteayer con el servicio que buscamos, ordenado por timestamp. Esto nos devolvera una lista de objetos donde los atributos de estos objetos seran el valor de cada fila.

        condition = and_(tableFut.timestamp>today ,tableFut.timestamp<=nextday)
        #condition= tableFut.timestamp < today ## provicional
        orderer =  tableFut.timestamp.asc()

        objs= QS.read_filter(db_F,tableFut,condition,orderer)
        if len(objs) == 0: 
            return False,objs

        if tableFut.__table__.name == 'bess_parameter_input' or tableFut.__table__.name == 'electricitycharges':

             #creamos una lista con los atributos de la tabla de pasado
            GetColumnPast=[ column.key for column in Past_table.__table__.columns]
            array={}
            for key in objs[0].__dict__.keys():
                        
                array[key]=""      
            

            ####concatenamos los valores de cada atributo en un array
            for obj in objs:        
            
                for key,value in obj.__dict__.items():
                    if key != "_sa_instance_state" and key!= "timestamp":
                        
                        val=str(array[key])
                        if val != "":
                            array[key] = val +"," + str(value)
                        else:
                            array[key]=str(value)

         

            # comparamos los atributos de la tabla de pasado con los de la tabla RT or Fut,
            # creando un diccionario solo de los atributos que coincidan de la tabla de pasado
            dict={}
            i=0
            for key, value in array.items(): 
                if key in GetColumnPast:
                    if "id_" in key:
                        pass
                    else:
                        if key != "timestamp":
                            dict[key]=value
                        else:
                            dict[key]=nextday
                    

            #almacenamos los valores contenido en el dictionary
            x=Past_table(**dict)        
            db_past.session.add(x)
            
            
        else:

            ### we obtains the names of the  FK_numberofset and typeof
            for key1 in objs[0].numberofset.__dict__.keys():
                if "TypeOf" in key1:
                    Typeof=key1

            for key2 in objs[0].__dict__.keys():
                if "FK_" in key2:
                    FK_name=key2
                    
        
            

            ##  make a Nested dictionary with the values obtains in obj
            NestedDist={}
            for obj in objs:

                # we obteins the value of the FK for each objet
                for FK_key, FK_value in obj.__dict__.items():
                    if "FK_" in FK_key:
                        FK_val=FK_value
                
                for obj_key,obj_value in obj.__dict__.items():
                    
                    if obj_key != FK_name and obj_key != "_sa_instance_state" and obj_key!= "timestamp":
                        if FK_val in NestedDist:
                            if obj_key in NestedDist[FK_val]:
                                str_value=str(NestedDist[FK_val][obj_key])
                                NestedDist[FK_val][obj_key] = str_value + "," + str(obj_value)
                            else:

                                NestedDist[FK_val][obj_key]= str(obj_value)
                        else:
                            NestedDist[FK_val]={obj_key:str(obj_value)}

                if Typeof == "TypeOfOutput":
                    NestedDist[FK_val][Typeof]= obj.numberofset.TypeOfOutput.name
                elif Typeof == "TypeOfInput":
                    NestedDist[FK_val][Typeof]= obj.numberofset.TypeOfInput.name
                            

                    
            
            #print(NestedDist)

        
            # make a list with the attribute of the table past
            
            GetColumnPast=list()
            for column in Past_table.__table__.columns:
                GetColumnPast.append(column.key)
                if "NumberOfSet_" in column.key:
                    NumberofSet= column.key
                

            # comparamos los atributos de la tabla de pasado con los de la tabla de FUT ,
            # creando un diccionario solo de los atributos que coincidan de la tabla de pasado
            
            
            for id, items in NestedDist.items(): 
                dict={}
                dict[NumberofSet] = id
                dict["timestamp"]= nextday

                for items_key,items_values in items.items():
                    if items_key in GetColumnPast:
                        dict[items_key]=items_values

                ##almacenamos los valores de cada dictionary creado
                x=Past_table(**dict)       
                db_past.session.add(x)
                            

        try: 
            db_past.session.commit() # cerramos sesion y enviamos todo.
            return True,objs
        except Exception as e:
            db_past.session.rollback()
            return e.args


    @staticmethod
    def OutputAcceptedFUT_to_OutputRT(db_RT,db_F,service,TableFut,tableRT):
        """""
        This method get the values of the table_FUT "output_accepted" filter by date and service and put on in the table_RT "output" but duplicated each value 12 time.

        Parameters
        ----------
        db_RT : flask_sqlalchemy.SQLAlchemy
            Configuration of a DB in SQLAlchemy of the Realtime database
        service : the type of service of TypeOfOutput
        TableFut = you must  insert the table 'classoutput_accepted_F'
        tableRT= you must  insert the table 'classoutput_R'
        year: year that we want obtains
        month: month that we want obtains
        day: month that we want obtains

        EXAMPLE:    db_RT: DB_R
                    service: 'ERMS'
                    TableFut: classoutput_accepted_F
                    TableRT: classoutput_R

                   

        Returns
        -------
        if the process is succesful return a list with true and objs  or the exeption print if an error
            has occured.
       
        """""
        
        now = datetime.datetime.now()
        today = datetime.datetime(year= now.year,month= now.month,day= now.day)
        deltatime_1_day = datetime.timedelta(days=1)
        nextday = today + deltatime_1_day
        column_fut=["Dispatch_P","Dispatch_Q","Dispatch_P_reserve_up","Dispatch_P_reserve_down","Dispatch_Q_reserve_up","Dispatch_Q_reserve_down"]
        condition= and_(TableFut.timestamp >today,TableFut.timestamp <= nextday)        # se buscan los datos del siguiente dia del dia actual

        
        objs=QS.read_filter(db_F,TableFut,condition)

        if len(objs) == 0: 
            return False,objs

        sumobj=[]
        for obj in objs:                    ## we make a array with the objects that contains our service

            if obj.numberofset.TypeOfOutput.name==service:
                sumobj.append(obj)


        ## make the dictionary with the values duplicated for each 5 minutes
        NestedDist={}
        delta=datetime.timedelta(minutes=5)
        h=datetime.timedelta(hours=0)
        for ob in sumobj:
            t=ob.timestamp
            while((ob.timestamp+delta*12)-t != h):
                for key,values in obj.__dict__.items():
                    if key in column_fut:
                        if t in NestedDist:
                            NestedDist[t][key]=values
                        else:
                            NestedDist[t]={key:values}

                t+=delta


        ## volcamos los valores de NestedDist a la tabla de RT

        for id, items in NestedDist.items(): 
            dict={}
            dict["timestamp"] = id
            dict["TypeOfOutput"] = service

            for items_key,items_values in items.items():
                if(items_key == column_fut[0]):
                    dict["P_activated"]=items_values

                elif(items_key ==column_fut[1]):
                    dict["Q_activated"]=items_values
                
                elif(items_key ==column_fut[2]):
                    dict["Limit_P_reserve_up"]=items_values

                elif(items_key ==column_fut[3]):
                    dict["Limit_P_reserve_down"]=items_values

                elif(items_key ==column_fut[4]):
                    dict["Limit_Q_reserve_up"]=items_values

                elif(items_key ==column_fut[5]):
                    dict["Limit_Q_reserve_down"]=items_values
                

            ##almacenamos los valores de cada dictionary creado
            x=tableRT(**dict)       
            db_RT.session.add(x)
                
              

        try: 
            db_RT.session.commit() # cerramos sesion y enviamos todo.
            return True,objs
        except Exception as e:
            db_RT.session.rollback()
            return e.args


    


    


        
        
            
