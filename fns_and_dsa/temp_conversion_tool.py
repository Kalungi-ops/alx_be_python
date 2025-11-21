FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

user_temp = float(input("Enter the temperature to convert: "))
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


C_or_F = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
if C_or_F == 'C'.lower():
    fah_temp = convert_to_fahrenheit(user_temp)
    print(f"{user_temp}°C is {fah_temp}°F")
elif C_or_F == 'F'.lower():
    cel_temp = convert_to_celsius(user_temp)
    print(f"{user_temp}°F is {cel_temp}°C")
else:
    print('Invalid temperature. Please enter a numeric value.')
