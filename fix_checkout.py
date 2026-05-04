with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_url = "https://pagamento.super-hits.com/checkout/v2/jrGksfVpnkiWBP8SUM9z"
new_url = "https://tilimcheckout.com/checkout?p=791e2db80319b586f356310496af7d1b"

count = content.count(old_url)
content = content.replace(old_url, new_url)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Substituido {count} link(s) de checkout!')
