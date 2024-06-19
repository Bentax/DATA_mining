import re
txt = "Пожалуйста, отправляйте свои заявки на адрес электронной почты inbox@example.com или по телефону 123456."
tokenize_regex = re.compile(r'((?:\w+@\w+\.\w+)|\w+|\S)', re.I)
tokens = tokenize_regex.findall(txt)
print(tokens)
#### ['Пожалуйста', ',', 'отправляйте', 'свои', 'заявки', 'на', 'адрес', 'электронной', 'почты', 'inbox@example.com', 'или', 'по', 'телефону', '123456', '.']
