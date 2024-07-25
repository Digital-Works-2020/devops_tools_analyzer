$(document).ready(function() {
   aws_account_name =  $('.account_name')[0].innerHTML.split(":")[1].trim();
   zone_id = $('.zone_id')[0].innerHTML.split(":")[1].trim();
   route53_hosted_zone_rec_url = "/aws/route53?account_name=" + aws_account_name  + "&data_to_extract=hosted_zones_record&zone_id=" + zone_id
   $.get(route53_hosted_zone_rec_url,function(data,status){
       if(data["status"] == 200)
       {
         hosted_zone_data = data["hosted_zone_records"]
         console.log(hosted_zone_data)
         $('#aws_hosted_zone_rec').DataTable({
            "data": hosted_zone_data,
            columns: [
                { data: 'name' },
                { data: 'type' },
                { data: 'ttl' },
                { data: 'values' },
            ],
        });
        $("table").show();
        $(".loader-container").hide();
       }
     }) 
}
)
