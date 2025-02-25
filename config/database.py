"""
Author: Jim Culbert
Copyright (c) 2021 MGHPCC
All rights reserved. No warranty, explicit or implicit, provided.
"""

import os
from regapp.config.env import ENV

# ------------------------------------------------------------------------------
# Database settings
# ------------------------------------------------------------------------------
# Set this using the DB_URL env variable. Defaults to sqlite.
#
# Examples:
#
# MariaDB:
#  DB_URL=mysql://user:password@127.0.0.1:3306/database  # pragma: allowlist secret
#
# Postgresql:
#  DB_URL=psql://user:password@127.0.0.1:8458/database  # pragma: allowlist secret
# ------------------------------------------------------------------------------
DATABASES = {
    'default': ENV.db_url(
        var='DB_URL',
        default='sqlite:///' + os.path.join(os.getcwd(), 'nercra.db')
    )
}


# ------------------------------------------------------------------------------
# Custom Database settings
# ------------------------------------------------------------------------------
# You can also override this manually in local_settings.py, for example:
#
# NOTE: For mysql you need to: pip install mysqlclient
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'coldfront',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     },
# }
#
# NOTE: For postgresql you need to: pip install psycopg2
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'coldfront',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }
