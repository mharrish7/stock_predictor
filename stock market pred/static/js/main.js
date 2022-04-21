
$('.spinner-border').hide();

$('.btn').on('click',function(){
    $('.spinner-border').fadeIn();
    $.ajax({
        type : 'POST',
        data : "h",
        url : '/pred'
    }).done(function(data){
        $('#date').text("For the next trading day of " + data['date'])
        if(data['d']){
            $('#res2').text("");
            $('#res1').text("IBM Stock is predicted to go " +  data['data']);
        }
        else{
            $('#res1').text("");
            $('#res2').text("IBM Stock is predicted to go " +  data['data']);
        }
        
    });

    $('.spinner-border').fadeOut();
});
