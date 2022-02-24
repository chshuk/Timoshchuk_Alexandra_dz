import sys

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.writelines(f'{int(sys.argv[1]):04d},{sys.argv[2][:2]}\n')
