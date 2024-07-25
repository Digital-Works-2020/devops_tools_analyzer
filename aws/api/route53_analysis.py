import boto3
from rest_framework.views import APIView
from rest_framework.response import Response
from aws.models import AWSAccount

class AWSRoute53Analyzer(APIView):
      def get(self, request, *args, **keyword_args):
          operation = self.request.query_params.get("data_to_extract")
          aws_account = self.request.query_params.get("account_name")
          zone_id = self.request.query_params.get("zone_id","")
          try:
               if operation == "route53" or operation == "hosted_zones":
                   result = list_of_operations[operation](aws_account)
                   result["status"] = 200
               elif operation  == "hosted_zones_record":
                   result = list_of_operations[operation](aws_account,zone_id)
                   result["status"] = 200
          except Exception as e:
              result = {}
              result["status"] = 500
              result["error"] = e
              print(result)
          return Response(result)

def get_client(service,access_key,secret_key,token=None):
    if token is None or token == "":
        return boto3.client(service,aws_access_key_id=access_key,aws_secret_access_key=secret_key)
    else:
       return boto3.client(service,aws_access_key_id=access_key,aws_secret_access_key=secret_key,aws_session_token=token)

def get_route53_analysis(account_name):
    aws_account = AWSAccount.objects.values_list().filter(account_name=account_name)[0]
    route53_client = get_client('route53',access_key=aws_account[1],secret_key=aws_account[2],token=aws_account[3])
    route53domains_client = get_client('route53domains',access_key=aws_account[1],secret_key=aws_account[2],token=aws_account[3])
      
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

def get_hosted_zones_analysis(account_name):
    aws_account = AWSAccount.objects.values_list().filter(account_name=account_name)[0]
    route53_client = get_client('route53',access_key=aws_account[1],secret_key=aws_account[2],token=aws_account[3])
    hosted_zone_data = []
    for hosted_zone in route53_client.get_paginator('list_hosted_zones').paginate():
        for each_hosted_zone in hosted_zone['HostedZones']:
            records_paginater = route53_client.get_paginator('list_resource_record_sets').paginate(HostedZoneId=each_hosted_zone['Id'])
            total_records = 0
            for each_record_page in records_paginater:
                total_records += len(each_record_page['ResourceRecordSets'])
            hosted_zone_data.append({
                              "id": each_hosted_zone['Id'].split("/")[-1],
                              "name": each_hosted_zone['Name'],
                              "description": each_hosted_zone["Config"].get('Comment',""),
                              "privateZone": each_hosted_zone["Config"]['PrivateZone'],
                              "total_records": total_records,
                              })
    return {"hosted_zone_data" : hosted_zone_data}

def get_hosted_zones_record(account_name,zone_id):
    aws_account = AWSAccount.objects.values_list().filter(account_name=account_name)[0]
    route53_client = get_client('route53',access_key=aws_account[1],secret_key=aws_account[2],token=aws_account[3])
    hosted_zone_records = []
    records_paginater = route53_client.get_paginator('list_resource_record_sets').paginate(HostedZoneId=zone_id)
    for each_record_page in records_paginater:
        for each_record in each_record_page['ResourceRecordSets']:
            print(each_record)
            hosted_zone_records.append({
                 "name": each_record.get("Name","N/A"),
                 "type": each_record.get("Type","N/A"),
                 "ttl" : each_record.get("TTL","N/A"),
                 "values": ",".join([each_record_value["Value"] for each_record_value in each_record.get("ResourceRecords",[])]),
             })
    return {"hosted_zone_records" : hosted_zone_records}

list_of_operations = {
    "route53" : get_route53_analysis,
    "hosted_zones" : get_hosted_zones_analysis,
    "hosted_zones_record" : get_hosted_zones_record 
}
