from django.shortcuts import render
from django.http import HttpResponse
from aws.models import AWSAccount

def index(request):
    aws_objects = AWSAccount.objects.all()
    context = {
                 'aws_objects' : aws_objects
    }
    return render(request, "base.html",context)
