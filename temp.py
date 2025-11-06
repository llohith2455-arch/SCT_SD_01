def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def get_scale_input(prompt):
    print(prompt)
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    choice = input("Enter your choice (1/2/3): ")
    return int(choice)

def convert_temperature(value, from_scale, to_scale):
    if from_scale == to_scale:
        return value
    if from_scale == 1:  # Celsius
        if to_scale == 2:
            return celsius_to_fahrenheit(value)
        elif to_scale == 3:
            return celsius_to_kelvin(value)
    elif from_scale == 2:  # Fahrenheit
        if to_scale == 1:
            return fahrenheit_to_celsius(value)
        elif to_scale == 3:
            return fahrenheit_to_kelvin(value)
    elif from_scale == 3:  # Kelvin
        if to_scale == 1:
            return kelvin_to_celsius(value)
        elif to_scale == 2:
            return kelvin_to_fahrenheit(value)

def main():
    print("🌡️ Temperature Converter 🌡️")
    from_scale = get_scale_input("Choose the scale to convert FROM:")
    to_scale = get_scale_input("Choose the scale to convert TO:")
    value = float(input("Enter the temperature value: "))
    
    result = convert_temperature(value, from_scale, to_scale)
    print(f"Converted temperature: {result:.2f}")

if __name__ == "__main__":
    main()