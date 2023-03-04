# library imports (pip install)
import datetime
import base64
import io 

from dash import Dash, html, dcc

import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import plotly_express as px

app = Dash(__name__)

colors = {
    'background': '#7a64cf',
    'text': '#7a64cf'
}
app.layout = html.Div(style={'backgroundColor': colors['background']},
            children=[html.H1(children="Geocoding for Gorgeous Geography Girlies"),
            
            html.Div(children="Upload .csv or . xls"),

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
                'margin': '10px'
                },
            # Allow multiple files to be uploaded
            multiple=True
                        ),
            html.Div(id='Uploaded Data')
                    ])

if __name__ == '__main__':
    app.run_server(debug=True)
