import re

RE_EMAIL = re.compile(r'(?P<username>([a-z]+.*))@(?P<domain>([a-z]+.*)\.[a-z]+)')


def email_parse(email):
    email_dict = {}
    for result in RE_EMAIL.finditer(email):
        for key, val in result.groupdict().items():
            email_dict[key] = val
    if not email_dict:
        raise ValueError(f'неверный формат {email}')
    return email_dict


email_address = 'timoshchuk@alex-ra.ru'
print(email_parse(email_address))
email_address = 'al-ra@chshuru'
print(email_parse(email_address))
