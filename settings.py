import os

from FinalAttestation.api.api import BASE_DIR


INSTALLED_APPS = [
    # другие установленные приложения
    'debug_toolbar',
]

MIDDLEWARE = [
    # другие middleware
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    # Обычно это '127.0.0.1' для локальной разработки
    '127.0.0.1',
]

ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')