"""
Created 7/27/2025
Animal Shelter Dashboard
CRUD_test.py

Author: Anthony Baratti
Southern New Hampshire University
CS-499 Computer Science Capstone
Artifact Enhancement #3
Conversion from MongoDB to SQLite3

Purpose: A test script built to test CRUD.py to show that the functionality
for SQLite3 conversion works as intended. Is not part of the operation of the
AnimalShelterArtifact. Imports AnimalShelter class from CRUD to access
the CRUD operation functionality and passes correct parameters to ensure
the database responds as it is supposed to.
"""

from CRUD import AnimalShelter

##Connects to the created database animals
db = AnimalShelter('animals.db')

#define the test animal:
test_animal = {
    "animal_id": "TEST123",
    "animal_type": "Dog",
    "breed": "Test Breed",
    "name": "Test!",
    "color": "Red",
    "date_of_birth": "2023-01-01",
    "datetime": "2024-07-27 12:00:00",
    "monthyear": "July 2024",
    "sex_upon_outcome": "Neutered Male",
    "age_upon_outcome": "1 year",
    "outcome_type": "Adoption",
    "outcome_subtype": "Foster",
    "age_upon_outcome_in_weeks": 52.0,
    "location_lat": 30.2672,
    "location_long": -97.7431
}

#Create test
print("----CREATE----")
created = db.create(test_animal)
print(f'Created: {created}')

#Read test
print("\n----READ----")
read = db.read("animal_id = 'TEST123'")
print(f'Read: {read}')

#Update with new read test
print("\n----UPDATE----")
update = db.update("animal_id = 'TEST123'", {"name": "UpdatedTest!", "breed": "Updated Test Breed"})
print(f'# of rows updated: {update}')
read_update = db.read("animal_id = 'TEST123'")
print(f'Updated Animal: {read_update}')

#delete test with check
print('\n----DELETE----')
delete = db.delete("animal_id = 'TEST123'")
print(f'# of deleted rows: {delete}')
update_delete = db.read("animal_id = 'TEST123'")
print(f'Should be empty if deleted: ', update_delete)
