# Setup Dash
from dash import Dash

# Configure the necessary Python module imports for dashboard components
import dash_leaflet as dl
from dash import dcc
from dash import html
import plotly.express as px
from dash import dash_table
from dash.dependencies import Input, Output, State
import base64

# Configure OS routines
import os

# Configure the plotting routines
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Configure Database Object
#import AnimalShelter from CRUD
from CRUD import AnimalShelter


# Connect to database via CRUD Module
# keep parameters of username and password optional
db = AnimalShelter(userName=None, userPwd=None)

# class read method must support return of list object and accept projection json input
# sending the read method an empty document requests all documents be returned
df = pd.DataFrame.from_records(db.read({}))

# MongoDB v5+ is going to return the '_id' column and that is going to have an 
# invlaid object type of 'ObjectID' - which will cause the data_table to crash - so we remove
# it in the dataframe here. The df.drop command allows us to drop the column. If we do not set
# inplace=True - it will reeturn a new dataframe that does not contain the dropped column(s)
df.drop(columns=['_id'],inplace=True)

## Debug
# print(len(df.to_dict(orient='records')))
# print(df.columns)


#########################
# Dashboard Layout / View
#########################
app = Dash(__name__)

##Grazioso image
image_filename = 'Grazioso Salvare Logo.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div([
    html.Div(id='hidden-div', style={'display':'none'}),
    html.Center(html.B(html.H1('CS-340 Dashboard'))),
    html.Hr(),
    html.A([
        ##Sets image as GS Logo, sizes and centers it, and attaches URL to clicking image
        html.Center(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                        height = 200, width = 200))], href = 'https://www.snhu.edu', target = '_blank'),
    html.Br(),
    ##Unique Identifier
    html.Center(html.I(html.H1("Anthony Baratti -- Project II"))),
    html.Hr(),
    html.Div([
        ##Creates a set of radio buttons and allows passing the stored button to other functions
        dcc.Store(id='animal-store'),
        dcc.RadioItems(['Show All Preferred', 'Water', 'Mountain or Wilderness', 'Disaster or Rescue', 'Reset'],
                       'Show All Preferred', id='animal-store-input'),
        html.Div(id = 'current-store') 
    ]),
    html.Hr(),
    dash_table.DataTable(id='datatable-id',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=True,
        row_selectable="single", #allows single row to be selected
        selected_rows=[],
        filter_action="native",
        sort_action="native",
        page_action="native",
        page_current=0, #set start page
        page_size=5, #set rows per page
                    ),
    html.Br(),
    html.Hr(),
#This sets up the dashboard so that your chart and your geolocation chart are side-by-side
    html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        ##Pie chart
        html.Div(
            id='graph-id',
            className='col s12 m6',

            ),
        ##Geolocation map
        html.Div(
            id='map-id',
            className='col s12 m6',
            )
        ]),
    html.Br(),
    ##Unique Identifier at bottom for Project screenshot purposes
    html.Center(html.I(html.H1("Anthony Baratti -- Project II"))),
    html.Hr(),
])

#############################################
# Interaction Between Components / Controller
#############################################

#Function to retrieve the radio button selection
#passes the value as input to update_dashboard

##Reference:
##Plotly, (N.D.), Dash core components. Dash.plotly.com
##https://dash.plotly.com/dash-core-components
@app.callback(Output('animal-store','data'),
             Input('animal-store-input', 'value'))
def update_store(value):
        return value

## Function to sort by preferred breeds, using 
## Animal type, breed, sex upon outcome, age upon outcome in weeks
## Uses return value of update_store() function (this means when a radio
## button is selected, it will save that value and pass it to this function
## as its input, i.e. 'animal-store', 'data')
@app.callback(Output('datatable-id','data'),
        [Input('animal-store', 'data')])
def update_dashboard(filter_type):
        #Show All is set to default in app.layout
        if (filter_type == 'Show All Preferred'):
            df = pd.DataFrame.from_records(db.read(
                ## Using $or allows the filter of all the sub
                ## filter types by combining them all together
                ## This way the "Show All" button won't just
                ## Show every single animal, but only the preferred
                ## animals of the specific fields.
                {'$or': [{'animal_type':'Dog',
                'breed': {'$in': ['Labrador Retriever Mix','Chesapeake Bay Retriever',
                                      'Newfoundland']},
                'sex_upon_outcome': 'Intact Female',
                'age_upon_outcome_in_weeks': {'$gte':26.0, '$lte':156.0}},
                {'animal_type':'Dog',
                'breed': {'$in': ['German Shepherd', 'Alaskan Malamute',
                                      'Old English Sheepdog', 'Siberian Husky',
                                      'Rottweiler']},
                'sex_upon_outcome': 'Intact Male',
                'age_upon_outcome_in_weeks': {'$gte':26.0, '$lte':156.0}},
                {'animal_type':'Dog',
                'breed': {'$in': ['Doberman Pinscher', 'German Shepherd', 'Golden Retriever',
                                      'Bloodhound', 'Rottweiler']},
                'sex_upon_outcome': 'Intact Male',
                'age_upon_outcome_in_weeks': {'$gte':20.0, '$lte':300.0}}]}))                 
            
        ##Filter for Water training dogs
        elif (filter_type == 'Water'):
            df = pd.DataFrame.from_records(db.read(
                        {'animal_type':'Dog',
                        'breed': {'$in': ['Labrador Retriever Mix','Chesapeake Bay Retriever',
                                      'Newfoundland']},
                        'sex_upon_outcome': 'Intact Female',
                        'age_upon_outcome_in_weeks': {'$gte':26.0, '$lte':156.0}}))
            
        ##Filter for Mountain/Wilderness training dogs
        elif(filter_type == 'Mountain or Wilderness'):
            df = pd.DataFrame.from_records(db.read(
                        {'animal_type':'Dog',
                        'breed': {'$in': ['German Shepherd', 'Alaskan Malamute',
                                      'Old English Sheepdog', 'Siberian Husky',
                                      'Rottweiler']},
                        'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome_in_weeks': {'$gte':26.0, '$lte':156.0}}))
            
        ##Filter for Disaster/Rescue training dogs
        elif(filter_type == 'Disaster or Rescue'):
            df = pd.DataFrame.from_records(db.read(
                        {'animal_type':'Dog',
                        'breed': {'$in': ['Doberman Pinscher', 'German Shepherd', 'Golden Retriever',
                                      'Bloodhound', 'Rottweiler']},
                        'sex_upon_outcome': 'Intact Male',
                        'age_upon_outcome_in_weeks': {'$gte':20.0, '$lte':300.0}}))
        elif(filter_type == 'Reset'):
            df = pd.DataFrame.from_records(db.read({}))

        df.drop(columns=['_id'],inplace=True)
        return df.to_dict('records')


# Display the breeds of animal based on quantity represented in
# the data table
@app.callback(Output('graph-id', "children"),
        [Input('datatable-id', "derived_virtual_data")])
def update_graphs(viewData):

    ##FIXME: This bit of code throws a callback error
    ##  Where no data is found upon initial startup.
    ##  Once the default data is in place, the pie chart
    ##  functions correctly.

    ##Fix
    # Defensive check for data before displaying
    if not viewData:
        return [html.Div("No data to display")]

    df = pd.DataFrame.from_dict(viewData)
    return [
        dcc.Graph( 
            ##changes size dimensions of pie chart
            style={'width': '500px', 'height': '500px'},
            figure = px.pie(df, names='breed', title='Preferred Animals').update_layout(
            ##changes background color of pie chart
            {'plot_bgcolor': 'rgba(0,0,0,0.2)', "paper_bgcolor": "rgba(0, 0, 0, 0.2)"}) 
        )    
    ]


# This callback will highlight the entire row when a user selects the row (in blue)
#

@app.callback(Output('datatable-id', 'style_data_conditional'),
        [Input('datatable-id', 'selected_rows')])
def update_styles(selected_rows):
    if selected_rows is None:
        return []
    return [{
        'if': { 'row_index': i },
        'background_color': '#D2F3FF'
    } for i in selected_rows]


# This callback will update the geo-location chart for the selected data entry
# derived_virtual_data will be the set of data available from the datatable in the form of 
# a dictionary.
# derived_virtual_selected_rows will be the selected row(s) in the table in the form of
# a list. For this application, we are only permitting single row selection so there is only
# one value in the list.
# The iloc method allows for a row, column notation to pull data from the datatable
@app.callback(Output('map-id', "children"),
        [Input('datatable-id', "derived_virtual_data"),
         Input('datatable-id', "derived_virtual_selected_rows")])
def update_map(viewData, index):  
    if viewData is None:
        return
    elif index is None:
        return
    
    dff = pd.DataFrame.from_dict(viewData)
    
    ##Sets default row assignment
    if index is None or len(index) == 0:
        row = 0
    ##Sets selected row assignment
    else: 
        row = index[0]
    
# Austin TX is at [30.75,-97.48]
    return [
        #Map layout
        dl.Map(style={'width': '500px', 'height': '500px'},
           center=[30.75,-97.48], zoom=10, children=[
           dl.TileLayer(id="base-layer-id"),
           # Marker with tool tip and popup
           # Column 13 and 14 define the grid-coordinates for 
           # the map
           # Column 4 defines the breed for the animal
           # Column 9 defines the name of the animal
           dl.Marker(position=[dff.iloc[row,13], dff.iloc[row,14]],
              children=[
              dl.Tooltip(dff.iloc[row,4]),
              dl.Popup([
                 html.H1("Animal Name"),
                    html.P(dff.iloc[row,9])
             ])
          ])
       ])
    ]
if __name__ == "__main__":
    app.run(debug=True)




