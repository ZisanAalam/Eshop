from django.shortcuts import redirect, render
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password


#Signup Customer
def signup(request):
    if request.method=="POST":
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        upass = request.POST.get('password')

        customer = Customer(first_name=fname, 
                                last_name=lname, 
                                phone=phone, 
                                email=email, 
                                password=upass)

        values = {'first_name':fname, 'last_name':lname,'email':email,'phone':phone}

        #validate customer details
        error_msg = ValidateCustomer(customer)

        if not error_msg:
            #hashing password before customer is registered
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('home')
        else:
            data = {'error':error_msg,
                    'value':values
                    }
            return render(request, 'store/signup.html',data)
    else:
        return render(request, 'store/signup.html')



import re
def checkmail(email):  
    regex = '^[\w.+\-]+@gmail\.com$'

    return (re.search(regex,email))

def ValidateCustomer(customer):
    error_msg = None
    customer_exists = customer.isExists()
    if not customer.first_name:
        error_msg = 'First name is required'
    elif len(customer.last_name)<4:
        error_msg = 'First name must be 4 character long or more'
    elif not customer.last_name:
        error_msg = 'Last name is required'
    elif not customer.phone:
        error_msg = 'Phone number is required'
    elif len(customer.phone) != 10:
        error_msg = 'Phone number should be of 10 digit'
    elif not customer.email:
        error_msg = 'Email is required'
    elif customer.email:
        if not checkmail(customer.email):
            error_msg = "Please enter valid email address"
    if not customer.password:
        error_msg = 'Password is required'
    elif len(customer.password)<6:
        error_msg = 'Pasword must be atleast 6 character long'
    elif customer_exists:
        error_msg = "Email address already registered"

    return error_msg