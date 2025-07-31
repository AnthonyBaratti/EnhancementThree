"""
Created 7/27/2025
Animal Shelter Dashboard
load_animals_from_csv.py

Author: Anthony Baratti
Southern New Hampshire University
CS-499 Computer Science Capstone
Artifact Enhancement #3
Conversion from MongoDB to SQLite3

**NOTE: RUN ONLY ONCE
This script is meant to create the database table structure
using SQL query language (INSERT).

It will read the .csv into animals.db which will be used by the
CRUD and ShelterDashboard. Do NOT populate the table more than once
CRUD and ShelterDashboard do not call this file, so it must be
run from the command line.

cd path/to/file
python load_animals_from_csv.py

"""

import sqlite3
import pandas as pd

# Connect to local animals.db folder for database
conn = sqlite3.connect("animals.db")
cursor = conn.cursor()

#Establishes empty table with column headers and datatypes
cursor.execute(
    """CREATE TABLE IF NOT EXISTS animals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_id TEXT NOT NULL,
        animal_type TEXT NOT NULL,
        breed TEXT,
        name TEXT,
        color TEXT,
        date_of_birth TEXT,
        datetime TEXT,
        monthyear TEXT,
        sex_upon_outcome TEXT,
        age_upon_outcome TEXT,
        outcome_type TEXT,
        outcome_subtype TEXT,
        age_upon_outcome_in_weeks REAL,
        location_lat REAL,
        location_long REAL
    )"""
)

#Populate the table
cursor.execute("SELECT COUNT (*) FROM animals") ##Counts rows in table
if cursor.fetchone()[0] == 0: ##if table has 0 rows, ok to populate

    #Load the csv
    df = pd.read_csv("aac_shelter_outcomes.csv")

    #Go row by row in the df
    for _, row in df.iterrows():
        cursor.execute( ##Insert each row into animals
            """INSERT INTO animals (
                animal_id, animal_type, breed, name, color, 
                date_of_birth, datetime, monthyear, sex_upon_outcome,
                age_upon_outcome, outcome_type, outcome_subtype,
                age_upon_outcome_in_weeks, location_lat, location_long
                )
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["animal_id"],
                row["animal_type"],
                row["breed"],
                row["name"],
                row["color"],
                row["date_of_birth"],
                row["datetime"],
                row["monthyear"],
                row["sex_upon_outcome"],
                row["age_upon_outcome"],
                row["outcome_type"],
                row["outcome_subtype"],
                row["age_upon_outcome_in_weeks"],
                row["location_lat"],
                row["location_long"]
            )
        )

    conn.commit()
    print("Animals database populated to animals.db with aac_shelter_outcomes.csv")
else:
    print("animals.db already exists and is populated, skipping upload")



