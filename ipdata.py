import requests
api_address = ' https://api.ipdata.co?api-key=d004c29e7ca24f49ffa4a13d2a806e5d2bf7deeed2be28624f5b6f32'

json_data=requests.get(api_address).json()
ip=json_data['ip']
city=json_data['city']
postal=json_data['postal']
current_time=json_data['time_zone']['current_time']
print(ip)
print(city)
print(postal)
print(current_time)
