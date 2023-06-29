# unit converter
def convert_units(value, from_unit, to_unit):
    # Define conversion rates
    conversion_rates = {
        'kg': {'g': 1000, 'mg': 1_000_000, 'l': 1},
        'g': {'kg': 0.001, 'mg': 1000, 'l': 0.001},
        'mg': {'kg': 0.000001, 'g': 0.001, 'l': 0.000001},
        'l': {'kg': 1, 'g': 1000, 'mg': 1_000_000},
        'ml': {'l': 0.001},
        'l': {'ml': 1000}
    }

    # Check if units are valid
    if from_unit not in conversion_rates or to_unit not in conversion_rates:
        print("Invalid unit!")
        return

    # Perform conversion
    result = value * conversion_rates[from_unit][to_unit]
    return result


# testing