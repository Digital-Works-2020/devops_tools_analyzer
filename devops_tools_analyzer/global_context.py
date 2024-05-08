from aws.models import AWSAccount

def get_global_context(request):
    aws_objects = AWSAccount.objects.all()
    return {
        'aws_objects' : aws_objects
    }
