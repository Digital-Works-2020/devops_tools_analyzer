$(document).ready(function() {
   aws_account_name =  $('.account_name')[0].innerHTML.split(":")[1].trim();
   current_cost_api_url = "/aws/cost?account_name=" + aws_account_name + "&data_to_extract=total_cost"
   prev_cost_api_url = current_cost_api_url + "&period=prev"
   $.get(current_cost_api_url,function(data,status){
       if(data["status"] == 200)
       {
          console.log("Updating Current AWS Cost")
          $('.current_cost')[0].innerHTML = data["cost"] + "USD"
       }
       else
       {
          console.log("Updating Error Message")
          $('.current_cost')[0].innerHTML = "Error:" + data["error"]
       }       
   });
   $.get(prev_cost_api_url,function(data,status){
       if(data["status"] == 200)
       {
          console.log("Updating Current AWS Cost")
          $('.prev_cost')[0].innerHTML = data["cost"] + "USD"
       }
       else
       {
          console.log("Updating Error Message")
          $('.prev_cost')[0].innerHTML = "Error:" + data["error"]
       }
   });
}
)
