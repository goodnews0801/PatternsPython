def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Пример использования
celsius_temperature = 25
converted_to_fahrenheit = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} градусов Цельсия равны {converted_to_fahrenheit:.2f} градусам Фаренгейта")

fahrenheit_temperature = 77
converted_to_celsius = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} градусов Фаренгейта равны {converted_to_celsius:.2f} градусам Цельсия")
