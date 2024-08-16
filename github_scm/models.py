from django.db import models

class GithubOrg(models.Model):
    account_name = models.CharField(max_length=60,primary_key=True)
    org_name = models.TextField()
    user_token = models.TextField()
