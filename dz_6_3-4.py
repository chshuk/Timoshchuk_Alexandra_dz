from itertools import zip_longest
import json

users_hobby = {}
with open('users.csv','r',encoding='utf-8') as f1:
    with open('hobby.csv','r',encoding='utf-8') as f2:
        with open('users_hobby.json', 'w', encoding='utf-8') as f3:
            for line1, line2 in zip_longest(f1, f2):
                if line2 and line1:
                    key = ' '.join(line1.strip().split(','))
                    users_hobby[key] = line2.strip().split(',')
                elif line1:
                    key = ' '.join(line1.strip().split(','))
                    users_hobby[key] = None
                elif line2:
                    for key, val in users_hobby.items():
                        print(key + ': ', val)
                    json.dump(users_hobby, f3, ensure_ascii=False)
                    exit(1)
for key, val in users_hobby.items():
    print(key + ': ', val)
with open('users_hobby.json', 'w', encoding='utf-8') as f3:
    json.dump(users_hobby, f3, ensure_ascii=False, separators=('\n',': '))