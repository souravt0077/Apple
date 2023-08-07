$(document).ready(function () {
    $('.whish_btn').click(function (e) { 
       
        let prod_id = $('.prod_id').val()
        let btn = $(this)
        let token = $('input[name=csrfmiddlewaretoken]').val()

        

        $.ajax({
            type: "POST",
            url: "/wishlist/add-to-wishlist/",
            data: {
                'id':prod_id,
                csrfmiddlewaretoken:token
            },

            dataType: "json",
            success: function (response) {
                alert(response.status)
            }
        });
        
    });
});