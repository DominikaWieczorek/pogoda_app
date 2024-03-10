# Weather Info App README

## Overview 🚀
The Weather Info App is a Python application designed to fetch current weather data for a specified city using the Weather API. It provides the user with the current temperature, pressure, humidity levels, and a general weather overview translated into Polish. 
## Features
- Fetch current weather data for any city
- Display weather information including temperature, pressure, and humidity
- Provide a weather overview in both English and Polish
- Display weather condition emojis based on the current temperature

## Requirements 🚀
Before running this application, ensure you have the following installed:
- Python 3.6 or newer
- `requests` library for making HTTP requests
- `pandas` library for data manipulation and analysis
- `unidecode` library for ASCII transliterations of Unicode text
- `translate` library for translating text

## Usage 
1. Obtain a valid API key from [Weather API](http://api.weatherapi.com/).
2. Replace the `api_key` variable's value in the script with your Weather API key.
3. Run the script in your terminal or command prompt.
4. Enter the city you wish to get weather data from when prompted.
5. Select the specific data you wish to display by entering the corresponding number when prompted.

### Example: 🎇
```plaintext
Enter the city to get weather data from: London
Select what you want to display for London: 
1) Temperature
2) Pressure
3) Humidity
4) All above
Your choice: 4

Weather overwiew: Light rain (PL: Niewielkie opady deszczu)
🌤️
Temperature for London is: 8.0°C
Pressure for London is: 995.0 mb
Humidity for London is: 100%

Process finished with exit code 0

