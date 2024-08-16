from django.urls import include, re_path
from . import views
from .api.project_analysis import JIRAProjectAnalyzer
from .api.webhook_analysis import JIRAWebhookAnalyzer

urlpatterns = [
        re_path('project$',JIRAProjectAnalyzer.as_view()),
        re_path('webhook$',JIRAWebhookAnalyzer.as_view()),
        re_path(r'(?P<jira_account>\w+)$',views.jira_index , name='jira_accounts')
]
