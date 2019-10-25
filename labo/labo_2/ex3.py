kelvin_temp = float(input("Kelvin: "))

celsius_temp = kelvin_temp - 273.15
fahrenheit_temp = celsius_temp / (5/9) + 32

print(kelvin_temp, "K =", fahrenheit_temp, "°F =", celsius_temp, "°C")
# print("%f K = %f °F = %f °C" % (kelvin_temp, fahrenheit_temp, celsius_temp))