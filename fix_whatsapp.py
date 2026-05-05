with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = "https://api.whatsapp.com/send?phone=5531973436780&text=Ol%C3%A1!%20Gostaria%20de%20saber%20mais%20sobre%20o%20Pendrive%20Virtual%20Flashback."
new = "https://wa.me/message/SKBSPCWG6445D1"

count = content.count(old)
content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Substituido {count} link(s) do WhatsApp!')
