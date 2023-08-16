import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tiktok_scheduler.settings")
django.setup()
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiktok_scheduler.settings')

get_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_application,
    "https":get_application,
    # Just HTTP for now. (We can add other protocols later.)
})
