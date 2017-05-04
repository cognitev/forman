from django.contrib import admin
from models import *

class InputInline(admin.StackedInline):
    model = Input

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('header_message', 'download_submission', 'submissions_count')
    inlines = [InputInline]
    model = Survey

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Input)