# AnimalShelterArtifact Enhancement Three
![App Logo](AnimalShelterArtifact/Grazioso%20Salvare%20Logo.png)<br>
Grazioso Salvare is a webpage designed to filter and track dog breeds to be trained for rescue missions. Grazioso did research on the best types of animals (dog breeds, age, sex, ect) for training, and they want an application that easily parses a csv file into a database, then filters the contents to match their research. They also want visuals that help convey meaningful information, such as breed ratio (pie chart), relative information (name, sex, intake date, age, ect), and an interactive map for finding the animals via longitude and latitude.

#### Technologies
- Python 3.11
- Dash
- Plotly
- pandas
- SQLite3
- dash-leaflet

#### Features
- Filter dogs by breed, age, and suitability for training
- Visualize data with interactive tables, maps, and pie charts
- Built with Dash, Plotly, SQLite3, and pandas


## AnimalShelterArtifact Original
Original Artifact from CS-340 Client Server Development<br>
<br>[Original Artifact](https://github.com/AnthonyBaratti/EnhancementThree/tree/main/AnimalShelterArtifact)<br><br>
This artifact was designed using a CRUD.py and a ShelterDashboard.py.<br>
The CRUD.py contains Create, Read, Update, and Delete (CRUD) methods for performing database queries. It also establishes the connection to MongoDB. All of these are wrapped in the AnimalShelter Class which will be imported from the CRUD.py into the ShelterDashboard.py. The purpose of the file is to manage query requests, although the ShelterDashboard will only use the Read function and the database connection.<br><br>
The ShelterDashboard.py contains the weblayout and app controller for the database queries. The first section is the Dashboard Layout/View, which uses HTML coding to establish the view and parameters of the page. This includes a datatable for organizing the returned queries, a pie chart that utilizes Plotly, and an interactive geo-location map for pinning a user selected animal.<br><br>
The second section is the controller. It uses app.callback functions that are event listeners, which wait for various clicks within the app (radio buttons, map markers, or selecting a single row). The predefined radio buttons show which type of rescue animals the user might be looking for (i.e., training a water rescue dog or a mountain rescue dog). These filters are then attached to encoded queries looking for the specific matches that were provided by Grazioso research. The selected filter the calls the read function from the CRUD.py and passes the parameters to pull the required documents from the database table, then stores them in the dataframe on the ShelterDashboard.py. The dataframe, now populated with the records, feeds that data into the various components (pie chart, data table, etc).

## AnimalShelterArtifact Enhancement
[Enhanced Artifact](https://github.com/AnthonyBaratti/EnhancementThree/tree/main/AnimalShelterArtifactEnhancement) <br> <br>
The enhancement to the AnimalShelterArtifact keeps the same exact architecture, it just converts the database from MongoDB to a local SQLite3 animals.db file. Since the csv is very well structured, an SQL structure can be achieved (as opposed to a NoSQL structure). SQLite3 was chosen because it is versatile with queries, but also very light weight. Moreover, locally storing the database means that the entire application can be packaged for extremely easy and user friendly setup (requiring only downloading the application then running it without installing any packages or databases). The conversion does not change anything about the application except how the information is stored and received. Any features that display or collect the information (layout, graphs/tables/map, filter options, ect) remain the same.<br><br>
First, the conversion of CRUD.py removes the MongoDB connection and creates a local "animals.db" file to store the csv file into the table. Since the csv is loaded once, the database (.db) ships pre-loaded. However, the .csv and the load script are available should a user accidently delete the database. The [CRUD](https://github.com/AnthonyBaratti/EnhancementThree/blob/main/AnimalShelterArtifactEnhancement/CRUD.py) functions have be reformatted to SQL clauses. Then, the [filter options](https://github.com/AnthonyBaratti/EnhancementThree/blob/main/AnimalShelterArtifactEnhancement/ShelterDashboard.py#L142) within the app.callback for the filters have been restructured to follow the SQL clause format as well. Since there is only controlled user input (i.e., only buttons, no text input), there is no need to safeguard entries. However, placeholders have been created to showcase security measures to prevent SQL Injection. The SQL structure follows the same procedures that the MongoDB structure enforced, searching by key and returning the values to the dataframe.<br><br>
Some added files for the enhancement include a CRUD_test.py, which ensures that every CRUD operation works as intended with a simple script test. A main.py was created that imports the ShelterDashboard to help control entry to the application with a single point. This py file also opens the web browser when the application is launched so the user does not have to. A main.spec that can be rebuilt with PyInstaller to rebuild the deployable .exe file in case changes are made to.<br> <br>
Libraries required to create the program: <br>
pip install dash dash-leaflet pandas plotly sqlite3 //for all functionality <br>
pip install pyinstaller   //For creating .exe
# TO RUN THE PROGRAM:

### Download the Enhanced main.exe
To run the application, simply download the dist.zip into an appropriate folder. Extract the contents then open the dist folder and double click main.exe <br>
This will open a web browser and launch the Dashboard within the browser.<br>
[Download the Grazioso Salvare Application (dist.zip)](https://github.com/AnthonyBaratti/EnhancementThree/releases/latest)
