from django.urls import include, re_path
from . import views
from .api.github_analysis import GithubAnalyzer

urlpatterns = [
        re_path('org_details$',GithubAnalyzer.as_view()),
        re_path(r'(?P<github_account>\w+)$',views.github_index , name='github_accounts')
]
