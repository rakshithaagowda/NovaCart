import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
from django.test import Client

django.setup()

c = Client()
resp = c.get('/', HTTP_HOST='localhost')
print('ROOT status', resp.status_code)
print('TEMPLATES RENDERED:')
for t in resp.templates:
    print(' -', getattr(t, 'name', None))

body = resp.content.decode('utf-8', errors='replace')
for idx, line in enumerate(body.splitlines(), 1):
    if '/logout/' in line or 'logout' in line and 'href' in line:
        print(f'BODY LINE {idx}: {line}')

print('--- RESPONSE CONTAINS <a href="/logout/"? ---', '<a href="/logout/"' in body)
print('--- RESPONSE CONTAINS href="/logout/"? ---', 'href="/logout/"' in body)
print('--- RESPONSE CONTAINS /logout/? ---', '/logout/' in body)
