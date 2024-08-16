from github import Github
from rest_framework.views import APIView
from rest_framework.response import Response
from github_scm.models import GithubOrg

class GithubAnalyzer(APIView):
      def get(self, request, *args, **keyword_args):
          operation = self.request.query_params.get("data_to_extract")
          github_account = self.request.query_params.get("account_name")
          result = {}
          try:
               if operation == "account_analysis":
                   result["data"] = list_of_operations[operation](github_account)
                   result["status"] = 200
          except Exception as e:
              print("Exception in Github Analysis Get API")
              result["status"] = 500
              result["error"] = e
              print(e)
          return Response(result)

def get_github_org_details(account_name):
    # Fetch Github Account
    github_account = GithubOrg.objects.values_list().filter(account_name=account_name)[0]
    
    org_name = github_account[1]
    api_token = github_account[2]
   
    #Github Object
    github_obj = Github(api_token)
    
    #Create Org Object
    org_obj = github_obj.get_organization(org_name)
    
    #Init Counters
    public_repos_count = 0
    private_repos_count = 0
    users_count = 0
    teams_count = 0

    # Get public repositories
    public_repos = org_obj.get_repos(type='public')
    for repo in public_repos:
        public_repos_count += 1

    # Get private repositories
    private_repos = org_obj.get_repos(type='private')
    for repo in private_repos:
        private_repos_count += 1
    
    # Get users in the organization
    members = org_obj.get_members()
    for member in members:
        users_count += 1
   
     # Get teams (groups) in the organization
    teams = org_obj.get_teams()
    for team in teams:
        teams_count += 1
    return {
        "public_repos"  : public_repos_count,
        "private_repos" : private_repos_count,
        "members_count" : users_count,
        "teams_count"   : teams_count,
    }
 
list_of_operations = {
    "account_analysis" : get_github_org_details
}
