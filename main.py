from weather_modules import WeatherModule

from weather_modules.get_weather_action import GetWeatherAction


if __name__ == "__main__":
    module = WeatherModule()
    module.register(GetWeatherAction, "GetWeatherAction")
    module.run()
