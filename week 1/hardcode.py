def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def weather_model(celsius_temperature):
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

    if fahrenheit_temperature < 32:
        return "Very cold weather."
    elif 32 <= fahrenheit_temperature < 50:
        return "Cold weather."
    elif 50 <= fahrenheit_temperature < 68:
        return "Moderate weather."
    elif 68 <= fahrenheit_temperature < 86:
        return "Warm weather."
    else:
        return "Hot weather."

# Example with hard-coded variables
hard_coded_temperature = 20
result = weather_model(hard_coded_temperature)
print(result)
