// using jquery for add to cart

$(document).ready(function () {
    $(".cart_btn").click(function (e) { 
        // e.preventDefault();
        let prod_id = $(this).closest('.product_data').find('.prod_id').val() // getting product id
        let prod_qty = $(this).closest('.product_data').find(".prod_qty").val() // getting quantity 
        let token = $(this).closest('.product_data').find('input[name=csrfmiddlewaretoken]').val()
        let btn = $(this)
        
        // let qty = $(this).closest('.product_data').find('.qty_input').val()

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
                // $(btn.html("Cart added"))
            }
        });


    });
    
});