import re

def parse(texto):
    regex = r"^(?P<ranking>\d+)\.\s*(?P<book>[\w\s,.:;-]+?)(?:\s+by\s+(?P<author>[\w\s]+))?\s\((?P<views>\d+)\)$"
    match = re.search(regex, texto)
    return (match[1], match[2], match[3], match[4])

test_cases = [
    (
        '2. Pride and Prejudice by Jane Austen (1481)',
        ('2', 'Pride and Prejudice', 'Jane Austen', '1481')
    ),
    (
        '1. Beowulf: An Anglo-Saxon Epic Poem (4903)',
        ('1', 'Beowulf: An Anglo-Saxon Epic Poem', None, '4903')
    )
]

for (texto, resultado) in test_cases:
    assert parse(texto) == resultado, f'Erro {texto}'