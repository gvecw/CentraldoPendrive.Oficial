import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Utmify script
content = re.sub(
    r'<script\s*[\s\S]*?cdn\.utmify\.com\.br[\s\S]*?</script>',
    '',
    content
)

# 2. Remove Microsoft Clarity script
content = re.sub(
    r'<script type="text/javascript">\s*[\s\S]*?clarity\.ms[\s\S]*?</script>',
    '',
    content
)

# 3. Remove UTM injection script at bottom (the (function() { const utms = ... block)
content = re.sub(
    r'<script>\s*\(function\(\)\s*\{[\s\S]*?utmify[\s\S]*?\}\)\(\);\s*</script>',
    '',
    content
)

# 4. Remove any leftover fbclid, gclid, utm injection scripts
content = re.sub(
    r'<script>\s*\(function\(\)\s*\{[\s\S]*?utm_source[\s\S]*?\}\)\(\);\s*</script>',
    '',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Todos os pixels de rastreamento removidos!')
