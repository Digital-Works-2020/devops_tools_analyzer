from django.shortcuts import render
from django.http import HttpResponse

def index(reques,aws_account):
    return HttpResponse("<h1>The AWS Homepage</h1>")
