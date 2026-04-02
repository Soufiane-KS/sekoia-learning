from pydantic.v1 import BaseModel, Field


# Module config — shared across all actions in this module
# Empty because wttr.in needs no API key
class WeatherModuleConfiguration(BaseModel):
    pass


# What the user sends to the action
class GetWeatherArguments(BaseModel):
    city: str = Field(..., description="City name to get weather for")


# What the action sends back
class GetWeatherResults(BaseModel):
    temperature: str = Field(..., description="Current temperature in Celsius")
    description: str = Field(..., description="Weather description")
    humidity: str = Field(..., description="Humidity percentage")
    wind_speed: str = Field(..., description="Wind speed in km/h")
