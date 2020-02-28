import re

texto = '2. Pride and Prejudice by Jane Austen (1481)'

#The Works of Edgar Allan Poe, The Raven Edition by Edgar Allan Poe (513)

result = re.search(r'(?P<ranking>\d+)\.\s*(?P<book>[\w\s]+?)\s+by\s+(?P<author>[\w\s]+)\((?P<views>\d+)\)', texto)

print(result.group('ranking'))
print(result.group('book'))
print(result.group('author'))
print(result.group('views'))