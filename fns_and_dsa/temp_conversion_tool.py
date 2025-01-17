FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return((fahrenheit -32) *  FAHRENHEIT_TO_CELSIUS_FACTOR)
def convert_to_fahrenheit(celsius):
    return((celsius *  CELSIUS_TO_FAHRENHEIT_FACTOR ) + 32)
def main():
    number = input("Enter the temperature to convert: ")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if unit == "C":
        result = convert_to_fahrenheit(float(number))
        print(str(number) + unit + "is " + str(result)+ "F")
    elif unit == "F":
        result = convert_to_celsius(float(number))
        print(str(number) + unit + "is " + str(result)+ "C")
    else:
        print("Invalid temperature. Please enter a numeric value.")
main()
