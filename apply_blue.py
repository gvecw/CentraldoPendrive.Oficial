with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Azul mais claro e vibrante - #40C4FF (sky blue neon)
content = content.replace('--primary: #2979FF;', '--primary: #40C4FF;')
content = content.replace('--primary-glow: rgba(41, 121, 255, 0.4);', '--primary-glow: rgba(64, 196, 255, 0.4);')
content = content.replace('#4d9aff 0%, #2979FF 100%)', '#74d7ff 0%, #40C4FF 100%)')
content = content.replace('background: linear-gradient(90deg, #1565C0, #2979FF);', 'background: linear-gradient(90deg, #0288D1, #40C4FF);')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Azul claro aplicado!')
