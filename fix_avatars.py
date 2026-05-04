with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Roberto Almeida - foto feminina, trocar para masculina
content = content.replace(
    'https://i.pravatar.cc/150?u=roberto',
    'https://i.pravatar.cc/150?img=12'
)

# Garantir que os outros tambem estao corretos
# Jaqueline - feminina (ok)
content = content.replace(
    'https://i.pravatar.cc/150?u=jaque',
    'https://i.pravatar.cc/150?img=47'
)
# Diego - masculino
content = content.replace(
    'https://i.pravatar.cc/150?u=diego',
    'https://i.pravatar.cc/150?img=68'
)
# Marcos - masculino
content = content.replace(
    'https://i.pravatar.cc/150?u=marcos',
    'https://i.pravatar.cc/150?img=57'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Avatares corrigidos!')
