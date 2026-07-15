import os
import sys
from pathlib import Path
import re

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from django.conf import settings
from django.test import Client
from django.contrib.auth.models import User

print('PROJECT_ROOT:', project_root)
print('TEMPLATE DIRS:', settings.TEMPLATES[0]['DIRS'])
print('TEMPLATE APP_DIRS:', settings.TEMPLATES[0]['APP_DIRS'])
print('INSTALLED_APPS:', settings.INSTALLED_APPS)
print('DEBUG:', settings.DEBUG)
print('BASE_DIR:', settings.BASE_DIR)
print('TEMPLATES root exists:', (project_root / 'templates').exists())
print('navbar exists:', (project_root / 'templates' / 'includes' / 'navbar.html').exists())
print('profile exists:', (project_root / 'templates' / 'store' / 'profile.html').exists())

print('\nSEARCHING ALL FILES FOR LOGOUT LINKS...')
patterns = [re.compile(r'href\s*=\s*["\\