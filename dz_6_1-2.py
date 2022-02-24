result = []
spamers = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = line.split(' ')[0]
        request = line.split('"')[1].split(' ')
        request_type: str = request[0]
        requested_resource = request[1]
        result.append((remote_addr, request_type, requested_resource))
        spamers[remote_addr] = spamers.setdefault(remote_addr, 0) + 1
for elem in result:
    print(elem)
value_spammer = max(spamers.values())
i = 0
for key, val in spamers.items():
    if val == value_spammer:
        i += 1
        print(f'Найден {i} спамер: IP - {key}, отправил {val} запросов')
