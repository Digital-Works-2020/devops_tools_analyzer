import boto3
from rest_framework.views import APIView
from rest_framework.response import Response
from aws.models import AWSAccount
from datetime import date,datetime
import calendar

class AWSCostAnalyzer(APIView):
      def get(self, request, *args, **keyword_args):
          operation = self.request.query_params.get("data_to_extract")
          aws_account = self.request.query_params.get("account_name")
          period = self.request.query_params.get("period","current")
          try:
               if operation == "total_cost":
                   result = list_of_operations[operation](aws_account,period)
                   result["status"] = 200
          except Exception as e:
              result = {}
              result["status"] = 500
              result["error"] = e
          return Response(result)

def get_total_cost(account_name,period="current"):
    aws_account = AWSAccount.objects.values_list().filter(account_name=account_name)[0]
    if aws_account[3] == "" or aws_account[3] is None:
        cost_client = boto3.client('ce',aws_access_key_id=aws_account[1],aws_secret_access_key=aws_account[2])
    else:
        cost_client = boto3.client('ce',aws_access_key_id=aws_account[1],aws_secret_access_key=aws_account[2],aws_session_token=aws_account[3])
    if period == "current":
        this_month_first = str(datetime.now().year) + "-" + str(datetime.now().month).zfill(2) + "-" + "01"
        response = cost_client.get_cost_and_usage(
               TimePeriod={ 'Start' : this_month_first ,'End' : str(date.today())},
               Granularity='MONTHLY',
               Metrics=['BlendedCost',],
        )
    else:
        if datetime.now().month == 1:
            prev_month = 12
            prev_year = datetime.now().year - 1
        elif datetime.now().month != 1:
            prev_month = datetime.now().month - 1
            prev_year = datetime.now().year
        Start = str(prev_year) + "-"  + str(prev_month).zfill(2) + "-" + "01" 
        End = str(prev_year) + "-"  + str(prev_month).zfill(2) + "-" + str(calendar.monthrange(prev_year,prev_month)[1])
        print(Start,End)
        response = cost_client.get_cost_and_usage(
               TimePeriod={ 'Start' : Start ,'End' : End},
               Granularity='MONTHLY',
               Metrics=['BlendedCost',],
        )
    return {"cost" : round(float(response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']),2) }
     

list_of_operations = {
    "total_cost" : get_total_cost 
}
