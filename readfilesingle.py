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

# Example with reading from a file (single set of input)
with open("temperature_input.txt", 'r') as file:
    file_input_temperature = float(file.readline())
result = weather_model(file_input_temperature)
print(result)
