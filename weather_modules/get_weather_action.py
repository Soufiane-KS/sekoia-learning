import requests
from sekoia_automation.action import Action
from weather_modules.models import GetWeatherArguments, GetWeatherResults


class GetWeatherAction(Action):
    results_model = GetWeatherResults

    def run(self, arguments: GetWeatherArguments) -> GetWeatherResults:
        self.log(
            message=f"Getting weather for: {arguments.city}", level="info"
        )

        response = requests.get(f"https://wttr.in/{arguments.city}?format=j1")

        if not response.ok:
            self.error(f"Weather API failed for {arguments.city}: {response.status_code}")

        data = response.json()
        current = data["current_condition"][0]

        return GetWeatherResults(
            temperature=current["temp_C"],
            description=current["weatherDesc"][0]["value"],
            humidity=current["humidity"],
            wind_speed=current["windspeedKmph"],
        )
