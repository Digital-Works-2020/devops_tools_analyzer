from django.shortcuts import render
from django.http import HttpResponse
import urllib
import re

def aws_index(request,**kwargs):
    context = {}
    decoded_url = urllib.parse.unquote(request.build_absolute_uri())
    match = re.search(r'aws_account=(\w+)', decoded_url)
    if match:
        context["aws_account"] = match.group(1)
    return render(request, 'aws_page.html',context)
