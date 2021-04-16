from django.shortcuts import redirect, render
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password

def user_login(request):
    if request.method == "GET":
        return render(request, 'store/login.html')
    else:
        email = request.POST.get('email')
        upass = request.POST.get('password')

        # fetch the user with the given email and match the password
    
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        
        if customer:
            flag = check_password(upass, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('home')
            else:
                error_msg = 'Invalid Password'
        else:
            error_msg = 'Invalid Email or Password'

        return render(request, 'store/login.html', {'error':error_msg})
