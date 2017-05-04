=====
forman
=====

forman is a simple Django app to create survery forms and collect and export submissions

Quick start
-----------

1. Add "forman" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'forman',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^forman/', include('forman.urls',namespace='forman')),

3. Run `python manage.py migrate` to create the forman models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a survey (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/survey/<survey_id> to fill in survey
6. Visit http://127.0.0.1:8000/survey/<survey_id>/download to download a csv of submissions