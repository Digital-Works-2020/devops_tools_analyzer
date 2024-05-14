import boto3
from rest_framework.views import APIView
from rest_framework.response import Response
from aws.models import AWSAccount

class AWSRoute53Analyzer(APIView):
      def get(self, request, *args, **keyword_args):
          operation = self.request.query_params.get("data_to_extract")
          aws_account = self.request.query_params.get("account_name")
          try:
               if operation == "route53":
                   result = list_of_operations[operation](aws_account)
                   result["status"] = 200
          except Exception as e:
              result = {}
              result["status"] = 500
              result["error"] = e
          print(result)
          return Response(result)

def get_route53_analysis(account_name):
    aws_account = AWSAccount.objects.values_list().filter(account_name=account_name)[0]
    if aws_account[3] == "" or aws_account[3] is None:
        route53_client = boto3.client('route53',aws_access_key_id=aws_account[1],aws_secret_access_key=aws_account[2])
        route53domains_client = boto3.client('route53domains',aws_access_key_id=aws_account[1],aws_secret_access_key=aws_account[2])
    else:
        route53_client = boto3.client('route53',aws_access_key_id=aws_account[1],aws_secret_access_key=aws_account[2],aws_session_token=aws_account[3])
        route53domains_client = boto3.client('route53domains',aws_access_key_id=aws_account[1],aws_secret_access_key=aws_account[2],aws_session_token=aws_account[3])
    
    #Calculate Hosted Zones
    total_hosted_zones = 0 
    result = {}
    for hosted_zone in route53_client.get_paginator('list_hosted_zones').paginate():
        total_hosted_zones += len(hosted_zone['HostedZones'])
    result["total_hosted_zones"] = total_hosted_zones
   
    #Calculate Total Domains
    total_domains = 0
    for domain in route53domains_client.get_paginator('list_domains').paginate():
        total_domains += len(domain['Domains'])
    result["total_domains"] = total_domains
    return result
    

list_of_operations = {
    "route53" : get_route53_analysis
}
