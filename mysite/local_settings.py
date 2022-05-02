import os

BASE_DIR = os.ppath.dirname(os.path.dirname(os.path.abspath(_file_)))

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

}
