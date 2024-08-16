from django.urls import include, re_path
from . import views

urlpatterns = [
        re_path(r'(?P<github_account>\w+)$',views.github_index , name='github_accounts')
]
