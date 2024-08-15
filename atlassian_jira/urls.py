from django.urls import include, re_path
from . import views
from .api.project_analysis import JIRAProjectAnalyzer

urlpatterns = [
        re_path('project$',JIRAProjectAnalyzer.as_view()),
        re_path(r'(?P<jira_account>\w+)$',views.jira_index , name='jira_accounts')
]
