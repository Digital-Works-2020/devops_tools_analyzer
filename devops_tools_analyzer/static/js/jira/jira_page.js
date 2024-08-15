$(document).ready(function() {
   jira_account_name =  $('.account_name')[0].innerHTML.split(":")[1].trim();
   
   project_api_url = "/jira/project?account_name=" + jira_account_name + "&data_to_extract=project_types"
   
   $.get(project_api_url,function(data,status){
       if(data["status"] == 200)
       {
          console.log("Updating Jira Projects")
          $('.business_projects')[0].innerHTML =  data["data"]["Business Projects"]
          $('.software_projects')[0].innerHTML =  data["data"]["Software Projects"]
          $('.team_projects')[0].innerHTML     =  data["data"]["Team Managed Projects"]
          $('.company_projects')[0].innerHTML  =  data["data"]["Company Managed Projects"]
          
       }
       else
       {
          console.log("Updating Error Message")
          $('.business_projects')[0].innerHTML =  "Failed to Process Data"
          $('.software_projects')[0].innerHTML =  "Failed to Process Data"
          $('.team_projects')[0].innerHTML =  "Failed to Process Data"
          $('.company_projects')[0].innerHTML =  "Failed to Process Data"
          console.log(data["error"])
       }       
   });
}
)
