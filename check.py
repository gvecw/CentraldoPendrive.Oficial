with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

checks = ['utmify', 'clarity.ms', 'utm_source', 'fbclid', 'gclid']
for c in checks:
    found = c.lower() in content.lower()
    status = 'ENCONTRADO' if found else 'LIMPO'
    print(c + ': ' + status)
