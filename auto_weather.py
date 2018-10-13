import requests
api_address = ' https://api.ipdata.co?api-key=d004c29e7ca24f49ffa4a13d2a806e5d2bf7deeed2be28624f5b6f32'
area = ''
json_data=requests.get(api_address).json()

area = json_data['city']
if (area == ''):
    area = json_data['country_name']
if (area == ''):
    print('Unable to fetch your location.')
    area = input("Enter city name=")
api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=4066962ccc1726d40a8699e13c5c0f78&q='
url = api_address + area

json_data=requests.get(url).json()
formatted_data=json_data['weather'][0]['main']
print("Your area=", area)
print(formatted_data)

