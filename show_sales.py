import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        print(f.read())
    if len(sys.argv) == 3:
        f.seek((int(sys.argv[1]) - 1) * 8)
        for _ in range(int(sys.argv[2]) - int(sys.argv[1]) + 1):
            print(f.readline().strip())
    if len(sys.argv) == 2:
        f.seek((int(sys.argv[1]) - 1) * 8)
        for line in f:
            print(line.strip())