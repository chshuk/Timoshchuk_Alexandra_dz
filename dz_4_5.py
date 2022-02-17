import sys
from utils import currency_rates

code_valute = sys.argv[1]
valute = currency_rates(code_valute)
print(f'на {valute[2]} курс {valute[0]} = {valute[1]} руб')
