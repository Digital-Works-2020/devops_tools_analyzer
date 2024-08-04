from django.urls import include, re_path
from . import views

urlpatterns = [
        re_path(r'(?P<jira_account>\w+)$',views.jira_index , name='jira_accounts'),
]
