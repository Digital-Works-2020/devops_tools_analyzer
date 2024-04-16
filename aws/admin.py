from django.contrib import admin

# Register your models here.
from .models import AWSAccount

admin.site.register(AWSAccount)
