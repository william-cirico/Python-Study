# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'João|Maria|adultos', texto))
print(re.findall(r'João|Maria|ad..tos', texto))
print(re.findall(r'[Jj]oão|[Mm]aria|adultos', texto))
print(re.findall(r'[a-zA-z]oão|[Mm]aria|adultos', texto))
print(re.findall(r'joÃo|MaRIa', texto, flags=re.I))
