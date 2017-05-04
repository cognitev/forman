##Install
pip install forman
in urls.py
url(r'^forman/', include('forman.urls',namespace='forman')),
in settings.py
INSTALLED_APPS = [
...
'forman',
...
]


##usage
you can link forman to any model

from forman import *

class poll(models.Model):
    survey = models.ForeignKey(Survey)