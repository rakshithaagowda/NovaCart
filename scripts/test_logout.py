import os
import sys
# Ensure project root is on sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from django.test import Client
from django.contrib.auth.models import User

username = 'testuser_for_logout'
password = 'testpass12345'
if not User.objects.filter(username=username).exists():
    User.objects.create_user(username=username, password=password)

c = Client()
print('Logging in...')
print('login result:', c.login(username=username, password=password))

resp = c.post('/logout/', follow=False, HTTP_HOST='localhost')
print('GET /logout/ status:', resp.status_code)
print('Headers:', {k:v for k,v in resp.items()})
print('Is redirect?', resp.status_code in (301,302,303))
if resp.status_code in (301,302,303):
    print('Location:', resp['Location'])

resp2 = c.post('/logout/', follow=True, HTTP_HOST='localhost')
print('Follow final status:', resp2.status_code)
print('Redirect chain:', resp2.redirect_chain)
print('Final URL (path):', resp2.request['PATH_INFO'])
print('User logged in after logout?', c.session.get('_auth_user_id') is not None)
