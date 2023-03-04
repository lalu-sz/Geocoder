import pandas as pd
from geopy.extra.rate_limiter import RateLimiter # delays between geocoding calls

df = pd.read_csv("addresses.csv")
print(df.head())
#print(df.columns)
'''[5 rows x 9 columns]
Index(['Unnamed: 0', 'Typ', 'Nr', 'Namn', 'Address1', 'Address3', 'Address4',
       'Address5', 'Telefon'],
      dtype='object')'''

geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
