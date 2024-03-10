import requests
import pandas as pd
from unidecode import unidecode
from translate import Translator
from datetime import datetime


# 1. Replace 'YOUR_API_KEY' with your API key from OpenWeatherMap
api_key = '62a6f5c5d0e24ed595791443240903'

# 2. Connect to API
while True:
    city = input("Enter the city to get weather data from: ")
    city_unidecoded = unidecode(city)
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_unidecoded}&aqi=yes'
    try:
        response = requests.get(url)  # get = select (in SQL)
        if response.status_code == 200:
            response = response.json()
            break
        else:
            if response.status_code == 400:
                print("Error! Invalid city input.")
    except:
        print("Unable to connect to API.")
        exit()

menu_message = f"Select what you want to display for {city}: " \
               "\n1. Temperature" \
               "\n2. Pressure" \
               "\n3. Humidity" \
               "\n4. All above" \
               "\nYour choice: "

while True:
    try:  # Jeżeli user poda wartość, którą uda się skonwertować do int -> przechodzimy do linijki 19
        user_choice = int(input(menu_message))
        if 0 < user_choice < 5:
            break
        else:
            print(f"{user_choice} is not supported option.")
    except ValueError:
        print("\nInvalid input. Try again!")

# 3. Prepare variables with weather information
temp_c = response['current']['temp_c']
pressure = response['current']['pressure_mb']
humidity = response['current']['humidity']

# 4. Display general weather overview message
translator = Translator(to_lang='pl')
weather_text = response['current']['condition']['text']
print(f"Weather overwiew: {weather_text} (PL: {translator.translate(weather_text)})")

# 5. Prepare funcion to display emojis
def display_weather_icon(temp):
    if temp_c > 15:
        print("☀️")
    elif temp_c <= 0:
        print("❄️")
    elif 15 > temp_c > 0:
        print("🌤️")

# 6. Display the retrieved data
if user_choice == 1:
    display_weather_icon(temp=temp_c)
    print(f"Temperature for {city} is: {response['current']['temp_c']}°C")
elif user_choice == 2:
    print(f"Pressure for {city} is: {response['current']['pressure_mb']} mb")
elif user_choice == 3:
    print(f"Humidity for {city} is: {response['current']['humidity']}%")
elif user_choice == 4:
    display_weather_icon(temp=temp_c)
    print(f"Temperature for {city} is: {response['current']['temp_c']}°C")
    print(f"Pressure for {city} is: {response['current']['pressure_mb']} mb")
    print(f"Humidity for {city} is: {response['current']['humidity']}%")

# 7. Save weather data do file
data = {'Miasto': city,
        'Temperatura °C': temp_c,
        'Ciśnienie': pressure,
        'Wilgotność': humidity,
        'Stan pogodowy': translator.translate(weather_text)
        }
#Create pandas dataframe
df = pd.DataFrame([data])

# Prepare date
current_date = datetime.now().strftime('%Y%m%d')

# Save data to excel file
excel_filename = f'dane_pogoda_{city.lower()}_{current_date}.xlsx' # lower - changes city name to lowercase
df.to_excel(excel_filename, index=False, engine='openpyxl')
