ALLOWED_HOSTS = ['*']

    'addressbook',

    ROOT_URLCONF = 'djangoapp.urls'

    WSGI_APPLICATION = 'djangoapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'addressbook',
	'USER': 'admin',
	'PASSWORD': 'password',
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
