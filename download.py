import urllib.request
import re

url = "https://super-hits.com/flashback/"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')
    
    # Replace relative URLs with absolute URLs for assets to load correctly from localhost
    html = re.sub(r'(src|href)="(/[^/][^"]*)"', r'\1="https://super-hits.com\2"', html)
    html = re.sub(r'(src|href)=\'(/[^/][^\']*)\'', r'\1=\'https://super-hits.com\2\'', html)
    html = re.sub(r'(src|href)="((?!http|data|#)[^"]+)"', r'\1="https://super-hits.com/flashback/\2"', html)
    html = re.sub(r'(src|href)=\'((?!http|data|#)[^\']+)\'', r'\1=\'https://super-hits.com/flashback/\2\'', html)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("Downloaded index.html")
