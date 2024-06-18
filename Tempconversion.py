##Temperature Conversion programme

#conversion from celcius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#conversion from celcius to kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

#conversion from fahrenheit to celcius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

#conversion from fahrenheit to kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

#Conversion from kelvin to celcius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

#conversion from kelvin to fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


#userinput(conditional statement)
def main():
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    temp = float(input("Enter the temperature value: "))

    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        print(f"{temp} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin.")
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        print(f"{temp} degrees Fahrenheit is equal to {celsius} degrees Celsius and {kelvin} Kelvin.")
    elif unit == 'K':
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        print(f"{temp} Kelvin is equal to {celsius} degrees Celsius and {fahrenheit} degrees Fahrenheit.")
    else:
        print("Invalid unit of measurement. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")

if __name__ == "__main__":
    main()
