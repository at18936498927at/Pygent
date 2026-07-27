import requests

from base_skill import BaseSkill


class WeatherSkill(BaseSkill):
    name = "weather"
    description = "Provides weather information for a given location."

    def get_weather(self, location: str) -> str:
        """
        Fetches the weather information for the specified location.

        Args:
            location (str): The location for which to get the weather.
        
        Returns:
            str: A string containing the weather information.
        """
        url = f"http://wttr.in/{location}?format=j1"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            current_condition = data['current_condition'][0]
            temp_c = current_condition['temp_C']
            weather_desc = current_condition['weatherDesc'][0]['value']
            return f"The current temperature in {location} is {temp_c}°C with {weather_desc}."
        except requests.RequestException as e:
            return f"Error fetching weather data: {e}.Response code: {response.status_code}" # pyright: ignore[reportPossiblyUnboundVariable]
        except (KeyError, IndexError) as e:
            return f"Error parsing weather data: {e}.Response code: {response.status_code}" # pyright: ignore[reportPossiblyUnboundVariable]
        return ""
