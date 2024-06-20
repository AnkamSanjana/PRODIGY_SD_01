def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
  """Converts Celsius to Kelvin."""
  return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
  """Converts Fahrenheit to Kelvin."""
  return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
  """Converts Kelvin to Celsius."""
  return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
  """Converts Kelvin to Fahrenheit."""
  return (kelvin - 273.15) * 9/5 + 32

# Get input from the user
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

# Convert the temperature
if unit == 'C':
  celsius = temperature
  fahrenheit = celsius_to_fahrenheit(temperature)
  kelvin = celsius_to_kelvin(temperature)
elif unit == 'F':
  fahrenheit = temperature
  celsius = fahrenheit_to_celsius(temperature)
  kelvin = fahrenheit_to_kelvin(temperature)
elif unit == 'K':
  kelvin = temperature
  celsius = kelvin_to_celsius(temperature)
  fahrenheit = kelvin_to_fahrenheit(temperature)
else:
  print("Invalid unit.")
  exit()

# Print the results
print(f"{temperature} {unit} is equal to:")
print(f"{celsius:.2f} Celsius")
print(f"{fahrenheit:.2f} Fahrenheit")
print(f"{kelvin:.2f} Kelvin")