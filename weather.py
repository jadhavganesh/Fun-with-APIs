import requests
api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=4066962ccc1726d40a8699e13c5c0f78&q='

city = input("Enter city name=")
url = api_address + city

json_data=requests.get(url).json()
formatted_data=json_data['weather'][0]['main']
print(json_data)
print(formatted_data)
