# library imports (pip install)
import datetime
import base64
import io 

from dash import Dash, html, dcc, dash_table

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

    dash_table.DataTable(
        df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
        style_as_list_view = False,
        style_cell={
            'backgroundColor': colors['background'],
            'color': colors['text'],
            'border': '1px solid pink' 
            }
        )       
]) # end of app layout


if __name__ == '__main__':
    app.run_server(debug=True)
