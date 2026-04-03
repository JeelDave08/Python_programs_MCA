class Temperature:
    
    # Convert Celsius to Fahrenheit
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    # Convert Fahrenheit to Celsius
    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius


# Example usage
temp = Temperature()

print("25°C to Fahrenheit:", temp.convertFahrenheit(25))
print("77°F to Celsius:", temp.convertCelsius(77))
