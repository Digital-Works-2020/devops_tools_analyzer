$(document).ready(function() {
   github_account_name =  $('.account_name')[0].innerHTML.split(":")[1].trim();
   
   github_api_url = "/github/org_details?account_name=" + github_account_name + "&data_to_extract=account_analysis"

   $.get(github_api_url,function(result,status){
       if(result["status"] == 200)
       {
          console.log("Updating Github Org Details")
          $('.public_projects')[0].innerHTML =  result["data"]["public_repos"]
          $('.private_projects')[0].innerHTML =  result["data"]["private_repos"]
          $('.total_users')[0].innerHTML =  result["data"]["members_count"]
          $('.total_teams')[0].innerHTML =  result["data"]["teams_count"]
       }
       else
       {
          console.log("Updating Error Message for Github Org Details")
          $('.public_projects')[0].innerHTML =  "Failed to Process Data"
          $('.private_projects')[0].innerHTML =  "Failed to Process Data"
          $('.total_users')[0].innerHTML =  "Failed to Process Data"
          $('.total_teams')[0].innerHTML =  "Failed to Process Data"
       }
   });

}
)
