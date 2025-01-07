def calculate_tax(bill,tax_rate):
    return round((bill * tax_rate)/100)


print(calculate_tax(200,13))