import os
import sys

from django.core.wsgi import get_wsgi_application

app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(os.path.join(app_path, 'loan_management'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "config.settings.production")

application = get_wsgi_application()
