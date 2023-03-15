# running in output window with code runner extension
# use CTRL + ALT + N to run

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter # delays between geocoding calls

# Creating geolocator by connecting to OSM Nominatim API
locator = Nominatim(timeout=10, user_agent="Geocoder") # Increasing timeout from 1 sec (default) to 10 sec

df = pd.read_csv("addresses.csv")
#print(df.head())
#print(df.columns)
'''[5 rows x 9 columns]
Index(['Unnamed: 0', 'Typ', 'Nr', 'Namn', 'Address1', 'Address3', 'Address4',
       'Address5', 'Telefon'],
      dtype='object')'''

# Creating a column in df that contains the full address
df['Full_Address']=df['Address1'].astype(str)+','+\
df['Address3'] +','+\
df['Address4'] +','+\
df['Address5'] +','+ 'Sweden'

print(df.loc[0,'Full_Address']) # using .loc function to get specific row in column)


'''calling the locator object to geocode with 1 sec delay 
      to avoid overloading server requests'''
geocode = RateLimiter(locator.geocode, min_delay_seconds= 1,)

df['GeoLoc'] = df.Full_Address.apply(geocode)

df['Lat'] = df.GeoLoc.apply(lambda x: locator.geocode(x).latitude if locator.geocode(x) != None else 'Null')
df['Long'] = df.GeoLoc.apply(lambda x: locator.geocode(x).longitude if locator.geocode(x) != None else 'Null')

df.to_csv('geocoded_output', columns={'GeoLoc','Lat','Long'})
