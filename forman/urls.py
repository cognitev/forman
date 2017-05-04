from django.conf.urls import url, include
import views
urlpatterns = [
    url(r'^survey/(?P<survey_id>[0-9]+)\/submit$', views.submit, name='submit'),
    url(r'^survey/(?P<survey_id>[0-9]+)\/download?', views.download_csv, name='download'),
    url(r'^survey/(?P<survey_id>[0-9]+)\/?', views.preview_survey, name='preview')
]
