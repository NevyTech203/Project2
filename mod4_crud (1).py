#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:55:26 2024

@author: nevenayoung_snhu
"""


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    def __init__(self, username, password):
        
        USER = 'aacuser'
        PASS = 'SNHU3214'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30680
        DB = 'AAC'
        COL = 'animals'
        USERNAME = USER
        PASSWORD = PASS
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connected succesfully to MongoDB")
        
        
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
            return True
           
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
    
    def read(self, query):
        if query is not None:
            cursor = self.database.animals.find(query)
            return list(cursor)
        else:
            return list
        
    def update(self, query, new_data):
        if query is not None:
            result = self.database.animals.update_one(query, new_data)
            if result.modified_count > 0:
                return result
            else:
                return False
        else:
            raise Exception("No query provided for update")
            
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_one(data)
            if result.deleted_count > 0:
                return result
            else: 
                return False
        else:
            raise Exception("No data provided for delete")
        
                
        