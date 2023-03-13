import os
import sys

# add the project directory to the sys.path
project_dir = "/var/www/html/clubweb1/clubweb"
sys.path.insert(0, project_dir)

# set the environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

# activate the virtual environment
activate_this = os.path.join(project_dir, 'venv/bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# import django
import django
django.setup()

# import the django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
