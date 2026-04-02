from sekoia_automation.module import Module
from weather_modules.models import WeatherModuleConfiguration


class WeatherModule(Module):
    configuration: WeatherModuleConfiguration
