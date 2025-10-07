def convert_length(value, unit_from, unit_to):
    units = {'m': 1, 'cm': 100, 'km': 0.001}
    return value * units[unit_to] / units[unit_from]

def convert_weight(value, unit_from, unit_to):
    units = {'kg': 1, 'g': 1000, 'lb': 2.20462}
    return value * units[unit_to] / units[unit_from]

def convert_temperature(value, unit_from, unit_to):
    if unit_from == 'C' and unit_to == 'F':
        return (value * 9/5) + 32
    elif unit_from == 'F' and unit_to == 'C':
        return (value - 32) * 5/9
    elif unit_from == 'C' and unit_to == 'K':
        return value + 273.15
    elif unit_from == 'K' and unit_to == 'C':
        return value - 273.15
    else:
        return value  # same unit

# Example usage
category = input("Choose category (length/weight/temperature): ").lower()
value = float(input("Enter value: "))
unit_from = input("From unit: ").lower()
unit_to = input("To unit: ").lower()

if category == 'length':
    result = convert_length(value, unit_from, unit_to)
elif category == 'weight':
    result = convert_weight(value, unit_from, unit_to)
elif category == 'temperature':
    result = convert_temperature(value, unit_from.upper(), unit_to.upper())
else:
    result = "Invalid category"

print("Converted value:", result)
