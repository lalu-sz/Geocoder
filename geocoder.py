# library imports (pip install)
import datetime
import base64
import io 

import dash
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output, State

import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import plotly_express as px

df = pd.read_csv('addresses.csv')

app = Dash(__name__)

colors = {
    'background': '#010902', # Black
    'text': '#e01f8c' # Strawberry
}
app.layout = html.Div(style={'backgroundColor': colors['background']},
    children=[html.H1(
        children="Geocoding for Gorgeous Geography Girlies", # Title
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ), # end of section

    html.Div(children="Upload .csv or . xls", style={
        'textAlign': 'center',
        'color': colors['text']
    }), # end of section

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
            ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'color': colors['text']
            },
            multiple=True # Allow multiple files to be uploaded
    ), # end of section

    html.Div(id='Uploaded Data',
            children= html.Div(['View Uploaded Data'])
    ), # end of section      
]) # end of app layout

'''Function for displaying uploaded user csv data'''
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try: 
        if 'csv' in filename:
            # if user uploads csv
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # is user uploads xls
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e: 
        print(e)
        return html.Div([
            'Error Processing Uploaded File :''('
        ])
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
        df.to_dict('records'),
        [{'name': i, 'id': i} for i in df.columns],
        style_as_list_view = False,
        style_cell={
            'backgroundColor': colors['background'],
            'color': colors['text'],
            'border': '1px solid pink' 
            }
        ),
        html.Hr(), # horizontal line

        # Display raw contents from web broswer
        html.Div('Raw Content'),
        html.Pre(contents[0:200]+ '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@app.callback(Output('Uploaded Data', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified'))

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None: 
        children = [
            parse_contents(c,n,d) for c, n, d in
            zip(list_of_contents,list_of_names,list_of_dates)]
        return children


if __name__ == '__main__':
    app.run_server(debug=True)
