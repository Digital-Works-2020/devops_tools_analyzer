from django.urls import include, re_path
from . import views
from .api.project_analysis import JIRAProjectAnalyzer
from .api.webhook_analysis import JIRAWebhookAnalyzer
from .api.plugin_analysis import JIRAPluginAnalyzer

urlpatterns = [
        re_path('project$',JIRAProjectAnalyzer.as_view()),
        re_path('webhook$',JIRAWebhookAnalyzer.as_view()),
        re_path('plugin$',JIRAPluginAnalyzer.as_view()),
        re_path(r'(?P<jira_account>\w+)/plugin_details', views.plugin_details,name='jira_plugin_details'),
        re_path(r'(?P<jira_account>\w+)$',views.jira_index , name='jira_accounts')
]
