from __future__ import unicode_literals

from django.db import models
from campaigns.models import Ad
from django.utils.html import format_html


class Survey(models.Model):
    header_message = models.CharField(max_length=200)
    header_image = models.FileField(blank=True, null=True)
    footer_message = models.CharField(max_length=200, blank=True)
    footer_image = models.FileField(blank=True, null=True)
    ad = models.OneToOneField(Ad, on_delete=models.CASCADE)
    def download_submission(self):
        return format_html(
            '<a href="/forman/survey/{}/download">download</a>',self.pk)

    def submissions_count(self):
        return self.submission_set.count()

    def __unicode__(self):
        return self.header_message

class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    columns = models.TextField()
    values = models.TextField()

class Input(models.Model):
    input_choices = (
    ('text', 'text'),
    ('image', 'image'),
    ('password', 'password'),
    ('radio', 'radio'),
    ('submit', 'submit'),
    ('reset', 'reset'),
    ('textarea', 'textarea'),
    ('file', 'file'),
    ('select', 'select'),
    ('multi-select', 'multi-select'),
    ('checkbox', 'checkbox'),
    )
    title = models.fields.CharField(max_length=200)
    display_type = models.fields.CharField(max_length=100, choices=input_choices)
    predefined_values = models.fields.TextField(blank=True, null=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    def predefined_list(self):
        if self.predefined_values:
            return self.predefined_values.split(",")
    def __unicode__(self):
        return "%s : %s" % (self.title, self.display_type)
