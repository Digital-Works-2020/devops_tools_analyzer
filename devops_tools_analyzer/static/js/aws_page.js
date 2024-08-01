$(document).ready(function() {
   aws_account_name =  $('.account_name')[0].innerHTML.split(":")[1].trim();
   
   current_cost_api_url = "/aws/cost?account_name=" + aws_account_name + "&data_to_extract=total_cost"
   prev_cost_api_url = current_cost_api_url + "&period=prev"
   groups_url = "/aws/iam?account_name=CS_Dev&data_to_extract=groups"
   route53_url = "/aws/route53?account_name=" + aws_account_name  + "&data_to_extract=route53"
   
   $.get(current_cost_api_url,function(data,status){
       if(data["status"] == 200)
       {
          console.log("Updating Current AWS Cost")
          $('.current_cost')[0].innerHTML = data["cost"] + " USD"
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
          console.log("Updating Previous Month AWS Cost")
          $('.prev_cost')[0].innerHTML = data["cost"] + " USD"
       }
       else
       {
          console.log("Updating Error Message")
          $('.prev_cost')[0].innerHTML = "Error:" + data["error"]
       }
   });
   $.get(groups_url,function(data,status){
       if(data["status"] == 200)
       {
          console.log("Updating Groups Details")
          $('.total_groups')[0].innerHTML = data["number_of_groups"]
          $('.empty_groups')[0].innerHTML = data["number_of_empty_groups"]
       }
       else
       {
          console.log("Updating Error Message")
          $('.total_groups')[0].inner_HTML = data["error"]
          $('.empty_groups')[0].inner_HTML = data["error"]
       }
   });   
   $.get(route53_url,function(data,status){
       if(data["status"] == 200)
       {
          console.log("Updating Hosted Zones & Domains Details")
          $('.total_hosted_zones')[0].innerHTML = data["total_hosted_zones"]
          $('.total_domains')[0].innerHTML = data["total_domains"]
       }
       else
       {
          console.log("Updating Error Message")
          $('.total_hosted_zones')[0].inner_HTML = data["error"]
          $('.total_domains')[0].inner_HTML = data["error"]
       }
   });    
}
)
