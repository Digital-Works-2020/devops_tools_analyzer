from django.urls import include, re_path
from . import views
from .api.cost_analysis import AWSCostAnalyzer
from .api.iam_analysis import AWSIAMAnalyzer
from .api.route53_analysis import AWSRoute53Analyzer

urlpatterns = [
        re_path(r'(?P<aws_account>\w+)/hostedzones/(?P<zone_id>\w+)', views.aws_zone_details, name='aws_zone'),
        re_path(r'(?P<aws_account>\w+)/hostedzones', views.aws_hosted_zones,name='aws_hosted_zones'),
        re_path('cost$',AWSCostAnalyzer.as_view()),
        re_path('iam$',AWSIAMAnalyzer.as_view()),
        re_path('route53$',AWSRoute53Analyzer.as_view()),
        re_path(r'(?P<aws_account>\w+)$',views.aws_index , name='aws_accounts'),
]
