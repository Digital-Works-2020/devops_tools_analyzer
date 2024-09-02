$(document).ready(function() {
   jira_account_name =  $('.account_name')[0].innerHTML.split(":")[1].trim();
   
   project_api_url = "/jira/project?account_name=" + jira_account_name + "&data_to_extract=project_types"
   webhook_api_url = "/jira/webhook?account_name=" + jira_account_name + "&data_to_extract=webhook_details"
   plugin_api_url  = "/jira/plugin?account_name=" + jira_account_name + "&data_to_extract=plugin_list"

   $.get(plugin_api_url,function(data,status){
       if(data["status"] == 200)
       {
          console.log("Updating Jira Plugins")
          $('.total_apps')[0].innerHTML = "<a href='/jira/"+ jira_account_name  + "/plugin_details'>" + data["data"]["plugin_count"] + "</a>"
       }
       else
       {
          console.log("Updating Error Message for Plugins")
          $('.total_apps')[0].innerHTML = "Failed to Process Data"
       }
   });

   $.get(webhook_api_url,function(data,status){
       if(data["status"] == 200)
       {
          console.log("Updating Jira Webhooks")
          $('.total_webhooks')[0].innerHTML =  data["data"]["total_webhooks"]
          $('.disabled_webhooks')[0].innerHTML =  data["data"]["disabled_webhooks"]
       }
       else
       {
          console.log("Updating Error Message for Webhooks")
          $('.total_webhooks')[0].innerHTML =  "Failed to Process Data"
          $('.disabled_webhooks')[0].innerHTML =  "Failed to Process Data"
       }
   });

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
          console.log("Updating Error Message for Jira Projects")
          $('.business_projects')[0].innerHTML =  "Failed to Process Data"
          $('.software_projects')[0].innerHTML =  "Failed to Process Data"
          $('.team_projects')[0].innerHTML =  "Failed to Process Data"
          $('.company_projects')[0].innerHTML =  "Failed to Process Data"
       }       
   });
}
)
