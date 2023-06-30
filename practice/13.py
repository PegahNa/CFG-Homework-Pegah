def report_weather(temperature, weather_func):
    return weather_func(temperature)


def as_sun_lover(temperature):
    if temperature >= 25:
        return "great"
    else:
        return "Not great"



def as_snow_lover(temperature):
    if temperature <= 0:
        return "great"
    else:
        return "Not great"


print(report_weather(24, as_sun_lover))
print(report_weather(25, as_sun_lover))
print(report_weather(25, as_snow_lover))
print(report_weather(1, as_snow_lover))
print(report_weather(0, as_snow_lover))