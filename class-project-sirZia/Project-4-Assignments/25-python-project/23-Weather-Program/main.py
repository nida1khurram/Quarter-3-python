# pip install requests
import requests
api_key = "9de5e751a71a5fed5badfc1bec107f54"
user_input = input("Enter City :")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api_key}")
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    # print(weather_data.status_code) # for checking purpose 200 mean yes
    # print(weather_data.json())

    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}")

    # temp = weather_data.json()['main']['temp']
    # print(weather, temp)  #for check