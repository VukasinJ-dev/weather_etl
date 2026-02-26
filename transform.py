import time
import pandas as pd
import logging
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def map_weather_code(code):
    """Converts numeric weather code to descriptive text."""
    weather_map = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        80: "Rain showers",
        81: "Heavy rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm"
    }
    
    return weather_map.get(code, "Unknown")

def get_missing_data(latitude, longitude):
    """Fetches current weather data for given coordinates."""
    
    url = f'https://api.open-meteo.com/v1/forecast'
    params = { 
        "latitude": latitude,
        "longitude": longitude,
        "current_weather":True
        }
    try:
        logging.info(f'Fetching data for latitude: {latitude}, longitude: {longitude}')
        response = requests.get(url = url, params=params,timeout=10)
        data = response.json()
        
        temperature = ''
        windspeed = ''
        weathercode = ''
        
        if 'error' in data:
            logging.warning(data['reason'])
        
        else:
            current = data.get('current_weather', {})
            
            temperature = current.get('temperature', '')
            windspeed = current.get('windspeed', '')
            weathercode = current.get('weathercode', '')
        logging.info(f'Data fetched for latitude: {latitude}, longitude: {longitude}')
        return {
            'temperature' : temperature,
            'windspeed' : windspeed,
            'weathercode' : map_weather_code(weathercode)
        }
    except requests.exceptions.ConnectionError:
        logging.error(f"Connection error")
        return {}
    
    except requests.exceptions.Timeout:
        logging.error(f"Timeout error")
        return {}
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return {}
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {}

def add_missing_columns(data):
    """Adds temperature, windspeed, and weather description columns to the DataFrame."""
    data['temperature'] = ''
    data['windspeed'] = ''
    data['weathercode'] = ''
    
    for row in data.itertuples():
        logging.info(f'Collecting data for {row.Index + 1}. row')
        missing_data = get_missing_data(row.latitude, row.longitude)
        
        if missing_data['temperature']:
            data.at[row.Index, 'temperature'] = missing_data['temperature']
        if missing_data['windspeed']:
            data.at[row.Index, 'windspeed'] = missing_data['windspeed']
        if missing_data['weathercode']:
            data.at[row.Index, 'weathercode'] = missing_data['weathercode']
        
        time.sleep(1)
    return data

def sort_data(data):
    """Sorts DataFrame by temperature in descending order."""
    logging.info(f'Sorting data by temperature.')
    data['temperature'] = pd.to_numeric(data['temperature'])
    return data.sort_values(by='temperature', ascending=False)

def generate_statistics(data):
    """Generates min, max, and average temperature statistics."""
    value_min_temp = data['temperature'].min()
    value_max_temp = data['temperature'].max()
    value_avg_temp = data['temperature'].mean()
    
    values = [{
        'value_min_temp' : value_min_temp,
        'value_max_temp' : value_max_temp,
        'value_avg_temp' : value_avg_temp
              }]
    
    new_df = pd.DataFrame(data=values)
    return new_df