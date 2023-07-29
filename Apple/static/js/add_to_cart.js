// using jquery for add to cart

$(document).ready(function () {
    $(".cart_btn").click(function (e) { 
        e.preventDefault();
        let prod_id = $('.prod_id').val() // getting product id
        let prod_qty = $(".prod_qty").val() // getting quantity 
        let token = $('input[name=csrfmiddlewaretoken]').val()
        let btn = $(this)

        $.ajax({
            type: "POST",
            url: "/cart/add-to-cart/",
            data: {
                'id':prod_id,
                'qty':prod_qty,
                csrfmiddlewaretoken:token
            },
            dataType: "Json",
            success: function (response) {
                alert(response.status)
                $(btn.html("Cart added"))
            }
        });


    });
});