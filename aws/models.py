from django.db import models

class AWSAccount(models.Model):
    account_name = models.CharField(max_length=60,primary_key=True)
    access_key = models.TextField(unique=True)
    secret_key = models.TextField(unique=True)
