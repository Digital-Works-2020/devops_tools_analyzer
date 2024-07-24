from django.shortcuts import render
from django.http import HttpResponse
import urllib
import re

def aws_zone_details(request,aws_account, zone_id):
    context = {}
    context["aws_account"] = aws_account
    context["zone_id"] = zone_id
    print(context)

def aws_hosted_zones(request,aws_account):
    context = {}
    context["aws_account"] = aws_account
    return render(request,'aws_route53_hosted_zones.html',context) 

def aws_index(request,aws_account):
    context = {}
    context["aws_account"] = aws_account
    return render(request, 'aws_page.html',context)
