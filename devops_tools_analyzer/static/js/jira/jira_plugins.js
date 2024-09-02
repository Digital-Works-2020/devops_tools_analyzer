$(document).ready(function() {
   jira_account_name =  $('.account_name')[0].innerHTML.split(":")[1].trim();
   jira_plugin_rec_url = "/jira/plugin?account_name=" + jira_account_name  + "&data_to_extract=plugin_list"
   $.get(jira_plugin_rec_url,function(data,status){
       if(data["status"] == 200)
       {
         jira_plugin_data = data["data"]["plugin_details"]
         $('#jira_plugin_rec').DataTable({
            "data": jira_plugin_data,
            columns: [
                { data: 'name' },
                { data: 'vendor' },
                { data: 'description' },
            ],
        });
        $("table").show();
        $(".loader-container").hide();
       }
     })
}
)
