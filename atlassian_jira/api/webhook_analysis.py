from jira import JIRA
from rest_framework.views import APIView
from rest_framework.response import Response
from atlassian_jira.models import JIRAAccount
import requests

class JIRAWebhookAnalyzer(APIView):
      def get(self, request, *args, **keyword_args):
          operation = self.request.query_params.get("data_to_extract")
          jira_account = self.request.query_params.get("account_name")
          result = {}
          try:
               if operation == "webhook_details":
                   result["data"] = list_of_operations[operation](jira_account)
                   result["status"] = 200
          except Exception as e:
              print("Exception in Webhook Analysis Get API")
              result["status"] = 500
              result["error"] = e
          return Response(result)

def get_webhook_details(account_name):
    # Fetch Jira Account
    jira_account = JIRAAccount.objects.values_list().filter(account_name=account_name)[0]
    user_email = jira_account[1]
    user_token = jira_account[2]
    jira_url = jira_account[3]
    
    #Init Web Hooks Var
    total_webhooks  = 0
    disabled_webhooks = 0

    #Setup Auth to get WebHook Details
    jira_auth = (user_email, user_token)
  
    #Webhook URL
    webhook_url = jira_url + "rest/webhooks/1.0/webhook" 
     
    #Retrieve WebHook Info
    webhook_response = requests.get(webhook_url,auth=jira_auth).json()
    
    #Parse Response
    for webhook in webhook_response:
        total_webhooks += 1
        if webhook["enabled"] == False:
            disabled_webhooks += 1
     
    #Return Response
    return {
        "total_webhooks"     : total_webhooks,
        "disabled_webhooks"  : disabled_webhooks
    }

list_of_operations = {
    "webhook_details" : get_webhook_details
}
