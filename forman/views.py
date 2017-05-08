from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_protect
from models import *
from django.core.mail import EmailMultiAlternatives
import csv
from django.conf import settings

def preview_survey(request, survey_id):
    context = {}
    the_survey = Survey.objects.get(pk = survey_id)
    inputs = Input.objects.filter(survey_id = survey_id)
    context['inputs'] = inputs
    context['survey'] = the_survey
    return render(request, "survey.html", context=context)

def create_submission(survey_id, params):
    columns = []
    values = []
    for key, value in params.items():
        if key != "csrfmiddlewaretoken":
            values_str = ",".join(value)
            columns.append(key)
            values.append(values_str)
    return Submission.objects.create(columns=";".join(columns), values=";".join(values), survey_id = survey_id)

@csrf_protect
def submit(request, survey_id):
    post_params = dict(request.POST.iterlists())
    submission = Context({"params":post_params})
    text_template = get_template('submit_email.txt')
    html_template = get_template('submit_email.html')
    text_format = text_template.render(submission)
    html_format = html_template.render(submission)
    subject, from_email = 'New Survey Submited', settings.FORMAN['sender_email']
    to = settings.FORMAN['receiver_emails']
    msg = EmailMultiAlternatives(subject, text_format, from_email, to)
    msg.attach_alternative(html_format, "text/html")
    msg.send()
    if create_submission(survey_id, post_params):
        #TODO respond with proper message!
        return HttpResponse("OK!")
    else:
        #TODO respond with proper message!
        return HttpResponse("OH!")

def download_csv(request, survey_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="survey'+survey_id+'_submissions.csv"'
    writer = csv.writer(response, delimiter="\t")
    index = 0
    for submission in Survey.objects.get(pk=survey_id).submission_set.all():
        if index < 1:
            writer.writerow( submission.columns.split(";") )
        writer.writerow(submission.values.split(";"))
        index+=1
    return response
