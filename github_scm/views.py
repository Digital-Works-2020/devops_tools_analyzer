from django.shortcuts import render
from django.http import HttpResponse
import urllib
import re

def github_index(request,github_account):
    context = {}
    context["github_account"] = github_account
    return render(request, 'github_page.html',context)
