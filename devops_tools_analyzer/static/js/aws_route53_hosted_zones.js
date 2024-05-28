$(document).ready(function() {
   aws_account_name =  $('.account_name')[0].innerHTML.split(":")[1].trim();
   route53_hosted_zone_url = "/aws/route53?account_name=" + aws_account_name  + "&data_to_extract=hosted_zones"
   $.get(route53_hosted_zone_url,function(data,status){
       if(data["status"] == 200)
       {

         $('#aws_hosted_zones').DataTable({
            "data": data["hosted_zone_data"],
            columns: [
                { data: 'name' },
                { data: 'description' },
                { data: 'id' },
                { data: 'privateZone' },
                { data: 'total_records' },
            ],
        });
        $("table").show();
        $(".loader-container").hide();
       }
     }) 
}
)
