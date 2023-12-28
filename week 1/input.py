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

# Example with keyboard input
keyboard_input_temperature = float(input("Enter the temperature in Celsius: "))
result = weather_model(keyboard_input_temperature)
print(result)
