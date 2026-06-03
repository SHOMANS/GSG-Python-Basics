def calculate_total(price, quantity, tax=0.15):
    net_total = price * quantity
    total = net_total + net_total * tax
    return total


print(calculate_total(100, 3))
