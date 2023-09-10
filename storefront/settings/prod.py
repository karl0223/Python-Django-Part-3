import dj_database_url
import os
from .common import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

DATABASE_URL = os.environ.get('DATABASE_URL')

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default=DATABASE_URL,
        conn_max_age=600
    )
}
