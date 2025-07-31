#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 07:30:55 2024

@author: anthonybaratt_snhu
"""

#Anthony Baratti
#Python CRUD Operations

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, userName=None, userPwd=None) -> None:
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        #
        # Connection Variables
        #

        HOST = 'localhost'
        PORT = 27017
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        # Here is a modification: Since we took away the userName and userPwd
        # that were previously used in the learning environment, adding an if else
        # statement allows the potential for credentials, but does not require them
        # as they no longer exist
        if userName and userPwd:
            # If a username and password are provided
            # Converted to string formatting for readability and best practice
            self.client = MongoClient(f'mongodb://{userName}:{userPwd}@{HOST}:{PORT}/')
        else:
            # if username and password not provided, connect to the host and port
            self.client = MongoClient(f'mongodb://{HOST}:{PORT}/')

        #Initializes database and collection
        self.database = self.client[DB]
        self.collection = self.database[COL]

# method to implement the C in CRUD.
    def create(self, createData=None) -> bool: #Constructs data to None if no data passed
        if createData:
            result = self.database.animals.insert_one(createData)  # data should be dictionary    
            return True if result.acknowledged else False #Returns true if data inserted
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        

# method to implement the R in CRUD.
    def read(self, readData) -> dict: #Constructs data to None if no data passed
        #No if statement for error checking. Returns entire DB if no data entered.
        result = list(self.database.animals.find(readData))
        return result#data should be dictionary

            
# method to implement U in CRUD
    def update(self, searchData=None, updateData = None):
        if searchData:
            result = self.database.animals.update_many(searchData, {"$set" : updateData})
            return result.modified_count
        else:
            raise Exception("Nothing to update, data parameter is empty")

# method to implement D in CRUD
    def delete(self, searchData=None):
        if searchData:
            result = self.database.animals.delete_many(searchData)
            return result.deleted_count
        else:
            raise Exception("Nothing to delete, data parameter is empty")
