from django.shortcuts import render
from django.http import HttpResponse
import urllib
import re

def jira_index(request,jira_account):
    context = {}
    context["jira_account"] = jira_account
    return render(request, 'jira/jira_page.html',context)
