from aws.models import AWSAccount
from atlassian_jira.models import JIRAAccount

def get_global_context(request):
    aws_objects = AWSAccount.objects.all()
    jira_objects = JIRAAccount.objects.all()
    return {
        'aws_objects' : aws_objects,
        'jira_objects' : jira_objects
    }
