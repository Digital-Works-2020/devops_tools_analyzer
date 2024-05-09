from django.urls import include, re_path
from . import views
from .api.cost_analysis import AWSCostAnalyzer
from .api.iam_analysis import AWSIAMAnalyzer

urlpatterns = [
        re_path(r'\?aws_account=(?P<aws_account>\w+)',views.aws_index , name='aws_accounts'),
        re_path('/cost$',AWSCostAnalyzer.as_view()),
        re_path('/iam$',AWSIAMAnalyzer.as_view()),
]
