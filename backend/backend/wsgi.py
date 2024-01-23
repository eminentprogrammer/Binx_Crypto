import os
import os
import environ
from pathlib import Path
from django.core.wsgi import get_wsgi_application

env = environ.Env(DEBUG=(bool, False))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))



os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('SERVER'))

application = get_wsgi_application()
