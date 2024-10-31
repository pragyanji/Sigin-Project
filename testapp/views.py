from django.shortcuts import render,redirect
from .models import Employees
from django.forms import model_to_dict
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def signin(request):
    if request.method == 'GET':
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
                return redirect('details',data)
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
        user = Employees.objects.filter(email = email)
        if user.exists():
            messages.info(request,'This user already exist')
            return redirect('signup')
        else:
            obj = Employees.objects.create(name = name,email = email,gender = gender,phone = phone,
                  state = state,password = password)
            obj.save()
            messages.info(request,'Data submitted successfully')
            return redirect(request,'success')  
    return render(request,'signup.html')

def success(request):
    return render(request,'success.html')

def logout(request):
    logout(request)
    return redirect('signin')
        
        
