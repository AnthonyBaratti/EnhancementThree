#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 7/27/2025
Animal Shelter Dashboard
CRUD.py

Author: Anthony Baratti
Southern New Hampshire University
CS-499 Computer Science Capstone
Artifact Enhancement #3
Conversion from MongoDB to SQLite3

Purpose: This script simply functions as the Create, Read,
Update, and Delete methods for the ShelterDashboard.py.
There is a test script: CRUD_test.py that will show
each method works, however only the READ method is used
in the ShelterDashboard.py.
"""


import sqlite3
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    ##Connect to database and create cursor
    def __init__(self, db_name="animals.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()



# method to implement the C in CRUD.
# @param dictionary data
# @return bool (success)
    def create(self, data: dict) ->bool:

        ##Ensures a dictionary key:value is passed
        if not isinstance(data, dict):
            raise TypeError("Data must be a dictionary")
        ##Ensures dictionary is not empty
        if not data:
            raise ValueError("Dictionary is empty")

        #Two fields in the CREATE TABLE definition are required (security practice)
        required_fields = ['animal_id', 'animal_type']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f'Missing required field: {field}')


        #create column "keys"
        columns = ", ".join(data.keys())
        #create placeholders for values (Helps negate injection)
        placeholders = ", ".join(["?"] * len(data))
        #collects the actual values for placeholders
        values = tuple(data.values())

        #insert the key:value pair into database
        self.cursor.execute(f"""
            INSERT INTO animals ({columns}) VALUES ({placeholders})
        """, values)
        self.conn.commit()
        return True
        

# method to implement the R in CRUD.
# @param string filter
# @return dict (uses zip to match column to row values)
    def read(self, filter: str = "") -> list[dict]: #uses filter option from ShelterDashboard

        #NOTE Since there is no text input from user (radio button filter), security is not needed
        #     here to prevent SQL Injection.
        base_query = "SELECT * FROM animals" ##Retrieves all columns
        if filter:
            base_query += f" WHERE {filter}" #if filter passed, restrict results to filter

        ##Perform read on database & return data
        self.cursor.execute(base_query)

        #get column names for any query using column names (i.e. 'location_lat')
        col_names = [desc[0] for desc in self.cursor.description]

        return [dict(zip(col_names, row)) for row in self.cursor.fetchall()]

            
# method to implement U in CRUD
# @param string field filter, dictionary new_data
# @return int updated rows
    def update(self, filter: str, new_data: dict) ->int: #accepts a filter for which row to update
        ##Ensures parameters are populated
        if not isinstance(new_data, dict) or not new_data:
            raise ValueError("Data must be non-empty dictionary")

        #columns to update
        update_clause = ", ".join([f'{key} = ?' for key in new_data.keys()])
        #values to update
        values = tuple(new_data.values())

        #SQL update statement to be passed to cursor
        #uses search query (filter) and keys to change (update_clause)
        sql_update = f'UPDATE animals SET {update_clause} WHERE {filter}'

        self.cursor.execute(sql_update, values)
        self.conn.commit()
        return self.cursor.rowcount #Number of rows that were updated.

# method to implement D in CRUD
# @param string filter
# @return int deleted rows
    def delete(self, filter: str) -> int:
        # ****NOTE!! It is vital to ensure data is passed here
        # if no data is passed, the entire table is deleted
        if not filter or not isinstance(filter, str):
            raise ValueError("Must have a filter string")

        #delete query by filter
        sql_delete = f'DELETE FROM animals WHERE {filter}'
        self.cursor.execute(sql_delete)
        self.conn.commit()

        return self.cursor.rowcount
