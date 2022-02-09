prices = [53.6, 5.34, 45.21, 67.9, 45.05, 34.66, 3.89, 121.56, 85.76, 65, 23,
          12.7, 3.78, 92.5, 137.87, 284.54, 45.98, 78.9, 3.6, 56.4, 100]
list_prices = []
print(prices)
string = ''
for price in prices:
    price = round(price * 100)
    list_prices.append(f'{price // 100} руб {(price % 100):02d} коп')
print(', '.join(list_prices))
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
sorted_prices = sorted(prices, reverse=True)
print(sorted_prices)
print(id(sorted_prices))
print('цены пяти самых дорогих товаров: ')
print(prices[len(prices)-5:])
