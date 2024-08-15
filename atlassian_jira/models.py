from django.db import models

class JIRAAccount(models.Model):
    account_name = models.CharField(max_length=60,primary_key=True)
    user_email = models.TextField()
    user_token = models.TextField()
    base_url = models.URLField(max_length=200)
