#pip install -U googlemaps
#pip install ipinfo
#pip install pyowm

from pyowm import OWM
import socket  
import ipinfo
import googlemaps
from pyowm import OWM
from datetime import datetime





def get_location():
    #TimeZone= details.Timezone()
    ipinfo_access_token= 'e987e3fa6c6b87'
    Google_Maps_API_KEY= 'AIzaSyD9zSrMqSoG4L6BkT-6eH5-XOiv5lfwJTU'
    OpenWeather_API_KEY= "c1931730fb94b1e8ae1b842f6c63665d"

    handler = ipinfo.getHandler(ipinfo_access_token)
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname) 
    details = handler.getDetails(IPAddr)
    lat,long= details.latitude, details.longitude

    city= details.city
    gmaps = googlemaps.Client(key=Google_Maps_API_KEY)
    reverse_geocode_result = gmaps.reverse_geocode((lat, long))
    address= reverse_geocode_result[0]['formatted_address']
    result= "City: {}, Street: {}".format(city, address)
    print(result)
    return result


def get_weather():
    ipinfo_access_token= 'e987e3fa6c6b87'
    Google_Maps_API_KEY= 'AIzaSyD9zSrMqSoG4L6BkT-6eH5-XOiv5lfwJTU'
    OpenWeather_API_KEY= "c1931730fb94b1e8ae1b842f6c63665d"
    handler = ipinfo.getHandler(ipinfo_access_token)
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname) 
    details = handler.getDetails(IPAddr)

    lat,long= details.latitude, details.longitude
    owm = OWM(OpenWeather_API_KEY)   
    mgr = owm.weather_manager()
    #observations= mgr.weather_around_coords(float(lat), float(long) )
    #print(observations)
    observation = mgr.weather_at_place(details.city)
    w = observation.weather
    #print(w.status)
    temperature= w.temperature('celsius')['temp']
    #print(temperature)

    if w.status == "Clear":
        weather_description= "sunny and clear"
    else:
         weather_description= w.status

    if temperature>25:
        weather_description+=", hot outside"
    elif temperature>7:
        weather_description+=", cool outside"
    elif temperature<7:
        weather_description+=", cold outside"
    elif temperature<0:
        weather_description+=", freezing outside"

    weather_description= weather_description+ ", "+ str(temperature) + " celsius"
    
    final_desc= "Weather: {}".format(weather_description)
    print(final_desc)
    return final_desc



get_location(details)
get_weather(details)