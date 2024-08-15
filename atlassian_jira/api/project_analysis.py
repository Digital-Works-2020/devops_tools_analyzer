from jira import JIRA
from rest_framework.views import APIView
from rest_framework.response import Response
from atlassian_jira.models import JIRAAccount

class JIRAProjectAnalyzer(APIView):
      def get(self, request, *args, **keyword_args):
          operation = self.request.query_params.get("data_to_extract")
          jira_account = self.request.query_params.get("account_name")
          result = {}
          try:
               if operation == "project_types":
                   result["data"] = list_of_operations[operation](jira_account)
                   result["status"] = 200
          except Exception as e:
              print("Exception in Project Analysis Get API")
              result["status"] = 500
              result["error"] = e
          return Response(result)

def get_project_types(account_name):
    # Fetch Jira Account
    jira_account = JIRAAccount.objects.values_list().filter(account_name=account_name)[0]
    user_email = jira_account[1]
    user_token = jira_account[2]
    jira_url = jira_account[3]
    
    # Initialize Counter Variables
    software_projects = 0
    business_projects = 0
    team_managed_projects = 0
    company_managed_projects = 0
    
    # Jira Object
    jira = JIRA(jira_url, basic_auth=(user_email, user_token))
    
    # Fetch Project & Fetch its types
    all_projects = jira.projects()
    for project in all_projects:
        # Check project type and style
        if project.projectTypeKey == 'software': 
            software_projects += 1
            if project.style == 'next-gen':
                team_managed_projects += 1
            elif project.style == 'classic':
                company_managed_projects += 1 
        elif project.projectTypeKey == 'business':
            business_projects += 1
            if project.style == 'next-gen':
                team_managed_projects += 1
            elif project.style == 'classic':
                company_managed_projects += 1
    return {
        'Software Projects': software_projects,
        'Business Projects': business_projects,
        'Team Managed Projects': team_managed_projects,
        'Company Managed Projects': company_managed_projects
    } 

list_of_operations = {
    "project_types" : get_project_types
}
