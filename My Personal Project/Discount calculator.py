price = float(input('Please input the price of the product:'))
discount = float(input('Please input the discount provided:'))

calc = price - ((discount/100) * price)

print(calc)
