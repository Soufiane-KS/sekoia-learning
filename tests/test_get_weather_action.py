import pytest

import requests_mock

from weather_modules.get_weather_action import GetWeatherAction
from weather_modules.models import GetWeatherArguments, GetWeatherResults


def test_get_weather_success(requests_mock):
    
    fake_weather_response = {
        "current_condition": [
            {
                "temp_C": "22",              # temperature in Celsius as a string
                "weatherDesc": [
                    {"value": "Sunny"}       # description is nested in a list of dicts
                ],
                "humidity": "45",            # humidity as a string
                "windspeedKmph": "15",       # wind speed as a string
            }
        ]
    }

    requests_mock.get(
        "https://wttr.in/Paris?format=j1",  # the URL to intercept
        json=fake_weather_response,          # return this as JSON
    )

    arguments = GetWeatherArguments(city="Paris")

    action = GetWeatherAction()
    result = action.run(arguments)

    if isinstance(result, dict):
        result = GetWeatherResults(**result)

    assert isinstance(result, GetWeatherResults)  # is it the right type?
    assert result.temperature == "22"              # did it extract temp_C?
    assert result.description == "Sunny"           # did it extract weatherDesc?
    assert result.humidity == "45"                  # did it extract humidity?
    assert result.wind_speed == "15"                # did it extract windspeedKmph?


def test_get_weather_api_failure(requests_mock):

    requests_mock.get(
        "https://wttr.in/InvalidCity?format=j1",
        status_code=500,  # server error
    )

    arguments = GetWeatherArguments(city="InvalidCity")
    action = GetWeatherAction()

    with pytest.raises(Exception):
        action.run(arguments)
