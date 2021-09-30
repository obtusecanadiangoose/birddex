import plotly.graph_objects as go
import dash
from dash.dependencies import Input, Output
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html
from dash import html
import sd_material_ui

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='myapplication')

mapbox_access_token = open(".mapbox_token").read()

fig = go.Figure(go.Scattermapbox(

        lat=['38.91427','38.91538','38.91458',
             '38.92239','38.93222','38.90842',
             '38.91931','38.93260','38.91368',
             '38.88516','38.921894','38.93206',
             '38.91275'],
        lon=['-77.02827','-77.02013','-77.03155',
             '-77.04227','-77.02854','-77.02419',
             '-77.02518','-77.03304','-77.04509',
             '-76.99656','-77.042438','-77.02821',
             '-77.01239'],
        mode="markers",
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=["The coffee bar","Bistro Bohem","Black Cat",
             "Snap","Columbia Heights Coffee","Azi's Cafe",
             "Blind Dog Cafe","Le Caprice","Filter",
             "Peregrine","Tryst","The Coupe",
             "Big Bear Cafe"],
    ))

fig.update_layout(clickmode='event+select')

fig.update_layout(
    #showlegend=False,
    margin={
        'l': 0,
        'r': 0,
        'b': 0,
        't': 0,
        'pad': 0,
    },
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        # dragRotate=False,
        style='mapbox://styles/mapbox/outdoors-v11',
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            # lat=38.92,
            lat=43.7059439,
            # lon=-77.07
            lon=-80.3779366
        ),
        pitch=0,
        zoom=10
    ),
)
app = dash.Dash(__name__)
'''
app = dash.Dash(
    '',
    external_stylesheets=[
        'https://fonts.googleapis.com/icon?family=Material+Icons',
    ]
)
'''

app.layout = html.Div([
    html.Div([
        dcc.Input(
            id="input1",
            type="text",
            placeholder="centre location",
            style={'width': '18vw', 'height': '5vh', 'float': 'right', 'margin': 'auto'}
        ),

        dcc.Graph(
            id='map',
            figure=fig,
            style={'width': '80vw', 'height': '90vh', 'float': 'left', 'margin': 'auto'},
            #clickData="string?"
        ),

    ]),
    html.Div([
        sd_material_ui.Button(
            children=html.P('Recentre Map'),
            id='button1',
            n_clicks=0,
            disableShadow=False,
            useIcon=False,
            variant='contained',
            style={'width': '18.5vw', 'height': '5vh', 'float': 'right', 'margin': 'auto'}
        ),
    ]),
    html.Div([
        sd_material_ui.Button(
            children=html.P('Add Marker'),
            id='button2',
            n_clicks=0,
            disableShadow=False,
            useIcon=False,
            variant='contained',
            style={'width': '18.5vw', 'height': '5vh', 'float': 'right', 'margin': 'auto'}
        ),
    ])
])

@app.callback(
    Output('map', 'figure'),
    Input('map', 'clickData'))
def display_click_data(clickData):
    print("clicked")
    return fig


app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter