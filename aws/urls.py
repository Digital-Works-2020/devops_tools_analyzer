from django.urls import include, re_path
from . import views
from .api.cost_analysis import AWSCostAnalyzer
from .api.iam_analysis import AWSIAMAnalyzer
from .api.route53_analysis import AWSRoute53Analyzer

urlpatterns = [
        re_path('\?aws_account=(?P<aws_account>\w+)/hosted_zones',views.aws_hosted_zones,name='aws_hosted_zones'),
        re_path(r'\?aws_account=(?P<aws_account>\w+)',views.aws_index , name='aws_accounts'),
        re_path('/cost$',AWSCostAnalyzer.as_view()),
        re_path('/iam$',AWSIAMAnalyzer.as_view()),
        re_path('/route53$',AWSRoute53Analyzer.as_view()),
]
