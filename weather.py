import requests




place_list = [(6.5244, 3.3792, 'Lagos'),(-22.908333, -43.196388, 'Rio de Janeiro'), (29.7604, -95.3698, 'Houston'), (30.0802, -94.1266, 'Beaumont'),(36.084090, -78.943310, 'Accura'),(25.761681, -80.191788, 'Miami'),(18.53917 , -72.335, 'Port-au-Prince'),(32.7765, -79.9311, 'Charleston'),(29.9511, -90.0715, 'New Orleans'),(4.061536, 9.786072, 'Douala'),]
# If you want to use classes
class Place:
  def __init__(self, lat, long, name):
    self.lat = lat
    self.long = long
    self.name = name

  def __str__(self):
    return(f'{self.name} latitude: {self.lat} longitude: {self.long} ') 

def create_placelist(list):
  places = []
  for city in list:
    place = Place(city[0], city[1], city[2])
    places.append(place)
  return places
    

places = create_placelist(place_list)


 


    

# would have attributes lat, long, name,
# Would be like a card in blackjack and the place_list would be like a deck


def get_weather_data(places):
  temp_data = {}
  for place in places:
    url = "https://api.climacell.co/v3/weather/realtime"
    payload = {
  "apikey": 'RPbgkXyTYWrBgOCU5Jyu4rLuWtPJdaIK',"lat":place.lat,
  "lon":place.long,
  "fields": ["temp", "humidity", "wind_gust","epa_health_concern"],
  "unit_system":"us", 

   }
    
    response = requests.get(url, params=payload).json()

    

    temp_data = response['temp'] ['value']

    wind_data = response['wind_gust']['value']
    humidity_data = response['humidity']['value']
    air_data = response['epa_health_concern']['value']

    

    print(f'The temperature in {place.name} is {temp_data}F. The wind gust is {wind_data} MPH, humidity is currently {humidity_data}% and the air quality is {air_data}')
    
get_weather_data(places)
