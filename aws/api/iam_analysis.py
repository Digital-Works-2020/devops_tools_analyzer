import boto3
from rest_framework.views import APIView
from rest_framework.response import Response
from aws.models import AWSAccount

class AWSIAMAnalyzer(APIView):
      def get(self, request, *args, **keyword_args):
          operation = self.request.query_params.get("data_to_extract")
          aws_account = self.request.query_params.get("account_name")
          try:
               if operation == "groups":
                   result = list_of_operations[operation](aws_account)
                   result["status"] = 200
          except Exception as e:
              result = {}
              result["status"] = 500
              result["error"] = e
          print(result)
          return Response(result)

def get_group_analysis(account_name):
    aws_account = AWSAccount.objects.values_list().filter(account_name=account_name)[0]
    if aws_account[3] == "" or aws_account[3] is None:
        iam_client = boto3.client('iam',aws_access_key_id=aws_account[1],aws_secret_access_key=aws_account[2])
    else:
        iam_client = boto3.client('iam',aws_access_key_id=aws_account[1],aws_secret_access_key=aws_account[2],aws_session_token=aws_account[3])
    groups = iam_client.list_groups()
    empty_groups = 0
    for group in groups['Groups']:
        if len(iam_client.get_group(GroupName=group['GroupName'])['Users']) == 0:
            empty_groups += 1
    result = {}
    result["number_of_groups"] = len(groups['Groups'])
    result["number_of_empty_groups"] = empty_groups
    return result
    

list_of_operations = {
    "groups" : get_group_analysis
}
