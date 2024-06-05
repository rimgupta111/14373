from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    if request.method == "POST":
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        mobile = request.POST.get('mbl')

        print("first_name---->", f_name)
        print("last_name---->", l_name)
        print("email---->", email)
        print("password---->", password)
        print("mobile---->", mobile)

        reg_obj = Registration(
            first_name = f_name,
            last_name = l_name,
            email = email,
            password = password,
            mobile = mobile,
        )
        reg_obj.save()


        
    return render(request,'home.html')