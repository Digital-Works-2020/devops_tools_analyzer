from django.shortcuts import render
from django.http import HttpResponse
from aws.models import AWSAccount
from atlassian_jira.models import JIRAAccount

def index(request):
    aws_objects = AWSAccount.objects.all()
    jira_objects = JIRAAccount.objects.all()    
    context = {
                 'aws_objects' : aws_objects,
                 'jira_objects' : jira_objects
    }
    return render(request, "base.html",context)
