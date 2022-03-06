import re

RE_LOG = re.compile(r'(?P<remote_addr>^([\w+\.])*)[\s-]+'
                    r'\[(?P<request_datetime>([^]]+))\]\s'
                    r'"(?P<request_type>([\w^\s]+))\s'
                    r'(?P<requested_resource>(.\w)+)\s'
                    r'\w+.+"\s(?P<response_code>(\d+))\s'
                    r'(?P<response_size>(\d+))\s')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # print(line)
        for result in RE_LOG.finditer(line):
            print(result.groupdict())
