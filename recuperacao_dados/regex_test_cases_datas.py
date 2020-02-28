import re

def parse(texto):
    regex = r"^(\d{1,2})[\/\-](\d{1,2})[\/\-](\d{2}|\d{4})$"
    match = re.search(regex, texto)
    return (match[1], match[2], match[3])

test_cases = [
    (
        '28/10/2019',
        ('28', '10', '2019')
    ),
    (
        '14/07/2019',
        ('14', '07', '2019')
    ),
    (
        '1/10/18',
        ('1', '10', '18')
    ),
    (
        '1/1/18',
        ('1', '1', '18')
    ),
    (
        '1-05-2019',
        ('1', '05', '2019')
    )
]

for (texto, resultado) in test_cases:
    assert parse(texto) == resultado, f'Erro {texto}'