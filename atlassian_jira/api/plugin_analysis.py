from jira import JIRA
from rest_framework.views import APIView
from rest_framework.response import Response
from atlassian_jira.models import JIRAAccount
import requests

class JIRAPluginAnalyzer(APIView):
      def get(self, request, *args, **keyword_args):
          operation = self.request.query_params.get("data_to_extract")
          jira_account = self.request.query_params.get("account_name")
          result = {}
          try:
               if operation == "plugin_list":
                   result["data"] = list_of_operations[operation](jira_account)
                   result["status"] = 200
          except Exception as e:
              print("Exception in Plugin Analysis Get API")
              result["status"] = 500
              result["error"] = e
          return Response(result)

def get_plugins_list(account_name):
    # Fetch Jira Account
    jira_account = JIRAAccount.objects.values_list().filter(account_name=account_name)[0]
    user_email = jira_account[1]
    user_token = jira_account[2]
    jira_url = jira_account[3]

    #Setup Auth to get Plugin Details
    jira_auth = (user_email, user_token)

    #Plugin URL
    plugin_url = jira_url + "rest/plugins/1.0/"
    
    #Retrieve Plugin Info
    plugin_response = requests.get(plugin_url,auth=jira_auth).json()

    #Plugin Counter
    plugin_count = 0
    plugin_details = []
    
    #Parse Response
    for plugin in plugin_response["plugins"]:
        if plugin["enabled"] == True and plugin["userInstalled"] == True:
            plugin_count += 1
            plugin_details.append(
               {
                   "name"        : plugin["name"],
                   "vendor"      : plugin["vendor"]["name"],
                   "description" : plugin["description"],
               }
            )
    
    return {
       "plugin_count"   : plugin_count,
       "plugin_details" : plugin_details
    } 

list_of_operations = {
    "plugin_list" : get_plugins_list
}
