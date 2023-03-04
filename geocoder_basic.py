# running in output window with code runner extension
# use CTRL + ALT + N to run

from geopy.geocoders import Nominatim

def geocode(address_input):
    '''geocodes input address'''
    #address_input = "433 Highland Ave NE, Atlanta, GA"
    
    geolocator = Nominatim(user_agent="geocoder_basic")
    location = geolocator.geocode(address_input)
    print(location.address)
    print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

#geocode("433 Highland Ave NE, Atlanta, GA")

def reverse_geocode():
    '''Reverse Geocoding (Coordinates to Address)'''
    lat_input = "33.761289500000004"
    long_input = "-84.3731535"
    coor_input = "{},{}".format(lat_input,long_input)

    geolocator = Nominatim(user_agent="geocoder_basic_reverse")
    location_r = geolocator.reverse(coor_input)
    print(location_r.address)

reverse_geocode()