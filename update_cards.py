with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Anos 70 - Pista de danca disco, bola de espelho, luzes coloridas
content = content.replace(
    'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?q=80&w=600&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?q=80&w=600&auto=format&fit=crop'
)

# Anos 80 - Neon, synthwave, cassete, visual retro anos 80
content = content.replace(
    'https://images.unsplash.com/photo-1598387181032-a3103a2db5b3?q=80&w=600&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?q=80&w=600&auto=format&fit=crop'
)

# Anos 90 - CD, grunge, festa anos 90
content = content.replace(
    'https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=600&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=600&auto=format&fit=crop'
)

# Romance - casal dançando, luzes suaves, clima romantico
content = content.replace(
    'https://images.unsplash.com/photo-1518609878373-06d740f60d8b?q=80&w=600&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?q=80&w=600&auto=format&fit=crop'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Imagens dos cards atualizadas!')
