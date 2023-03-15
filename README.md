# Geocoder 
Tutorials: 
    https://towardsdatascience.com/how-to-build-your-geocoding-web-app-with-python-133e1e9e2d1a
    https://towardsdatascience.com/things-to-do-with-latitude-longitude-data-using-geopy-python-1d356ed1ae30
    https://peterhaas-me.medium.com/how-to-geocode-with-python-and-pandas-4cd1d717d3f7

Resources:
Using VSCode/Code Spaces: 
    Output Window: https://stackoverflow.com/questions/62975030/how-to-use-output-in-vscode
Accessing specific records in df w/ .loc functions: 
    https://stackoverflow.com/questions/43772362/how-to-print-a-specific-row-of-a-pandas-dataframe
Getting Lat/Long attributes: 
    df.column.apply
    (
    lambda x: geolocator.geocode(x).latitude if geolocator.geocode(x) != None else 'NF'
    )
    https://stackoverflow.com/questions/53163909/python-pandas-geopyattributeerror-nonetype-object-has-no-attribute-latitude
df exports: 
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

Dash Elements: 
    HTML Cheatsheet: 
        https://htmlcheatsheet.com/
    dcc.Upload: app viewers can upload files:
        https://dash.plotly.com/dash-core-components/upload
    Layout Basics: 
        https://dash.plotly.com/layout


Random: 
    code 0 = finished running with no error


Formating Dash DataTable: 
dash_table.DataTable(
        df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
        style_as_list_view = False,
        style_cell={
            'backgroundColor': colors['background'],
            'color': colors['text'],
            'border': '1px solid pink' 
            }
        ) 