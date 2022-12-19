function add_new_customer(){
    var name = $('#name').val();
    var mobile = $('#mobile').val();
    var email = $('#email').val();
    var company_name = $('#company_name').val();
    var tax_number = $('#tax_number').val();
    var customer_address = $('#customer_address').val();
    var csrf_token = $("input[name='csrfmiddlewaretoken']").val();

    var data = {
        'name': name, 'mobile': mobile, 'email': email,
        'company_name': company_name, 'tax_number': tax_number,
        'customer_address': customer_address,
    }

    $.ajaxSetup(
        {
            data: {csrfmiddlewaretoken: csrf_token },
        }
    );

    $.ajax({
        url: '/customers/db/insert',
        method: 'post',
        data: data,
        success: function(response){
            alert(response['status']);
        },
        error:  function(response){
            alert(response);
        }
    });
}
