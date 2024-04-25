from django.shortcuts import render,redirect
from .models import Employees
from django.forms import model_to_dict
from django.contrib.auth import logout
# Create your views here.
def home(request):
    return render(request,'home.html')

def signin(request):
    if request.method == '':
        Email = request.GET.get('email')
        Password = request.GET.get('password')
        if Email:
            obj = Employees.objects.get(email = Email)
            data = model_to_dict(obj)
            password = data.get('password')
            if Password == password:
                name = data.get('name')
                email = data.get('email')
                phone = data.get('phone')
                state = data.get('state')
                gender = data.get('gender')

                data= {
                    'name':name,
                    'email':email,
                    'phone':phone,
                    'gender':gender,
                    'state':state,
                }
                return render(request,'details.html',data)
            else:
                message ={
                    'message':'Invalid password'
                }
                return render(request,'signin.html',message)
    return  render(request,"signin.html")

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        password = request.POST.get('password')
        
        obj = Employees(name = name,email = email,gender = gender,phone = phone,
                  state = state,password = password)
        obj.save()
        print('Data submitted successfully')
        return render(request,'success.html')
        
    return render(request,'signup.html')

def success(request):
    return render(request,'success.html')

def logout(request):
    logout(request)
    return redirect('signin')
        
        
