$(document).ready(function() {
   aws_account_name =  $('.account_name')[0].innerHTML.split(":")[1].trim();
   route53_hosted_zone_url = "/aws/route53?account_name=" + aws_account_name  + "&data_to_extract=hosted_zones"
   $.get(route53_hosted_zone_url,function(data,status){
       if(data["status"] == 200)
       {
         hosted_zone_data = data["hosted_zone_data"]
         for (let i = 0; i < hosted_zone_data.length; i++) {
             hosted_zone_data[i]["details"] = "/aws/"+ aws_account_name + "/hostedzones/" +hosted_zone_data[i]["id"]
         }
         $('#aws_hosted_zones').DataTable({
            "data": hosted_zone_data,
            columns: [
                { data: 'name' },
                { data: 'description' },
                { data: 'id' },
                { data: 'privateZone' },
                { data: 'total_records' },
                { data: 'details',
                  render: function (data, type) {
                             return "<a href=" + data + ">View Records</a>"
                          }
                },
            ],
        });
        $("table").show();
        $(".loader-container").hide();
       }
     }) 
}
)
