from django.shortcuts import render, redirect
from django.http import HttpResponse
from sc.models import FoodItem
from django.contrib.auth.models import User  # Correct import

# Create your views here.
def f(request):
    return HttpResponse("So many books, so little time.")

def func2(request):
    return HttpResponse("Nothing")

def fun(request, name):
    return HttpResponse(f"<h1>Hello {name}.</h1>")

def fun3(request):
    return redirect('home')

def func4(request, b):
    return HttpResponse(f'<h1>{b} {b} yes papa<br> eating sugar no papa<br>telling lies no papa<br> open our mouth Ha Ha...</h1>')

def index(request):
    return render(request, 'index.html')

def items(request):
    return render(request, 'items.html')

def about(request):
    return render(request, 'about.html')

def nitem(request):
    return render(request, 'nitem.html')

def table(request):
    li = [
        ["a", "csd", 0],
        ["b", "csd", 9],
        ["c", "cse", 10]
    ]
    context = {'data': li}
    return render(request, 'table.html', context)

def farenhit(request):
    if request.method == "POST":
        name = request.POST.get('b')
        d = {'a': (float(name) - 32) * 5 / 9}  # Corrected formula for Fahrenheit to Celsius
        return render(request, 'form.html', d)
    return render(request, 'form.html')

def f3(request):
    result = FoodItem.objects.all()[::-1]  # Use objects instead of object
    if request.method == "POST":
        dish = request.POST.get('dishname')
        cost = int(request.POST.get('dishprice'))
        obj = FoodItem(name=dish, price=cost)
        obj.save()
        return render(request, 'form2.html', {'data': result})
    return render(request, 'form2.html', {'data': result})

def addUser(request):
    if request.method == "POST":
        u = request.POST.get("usern")
        f = request.POST.get("fname")
        l = request.POST.get("lname")
        m = request.POST.get("email")  # Fixed variable name from f to m
        p = request.POST.get("password")  # Fixed variable name from u to p
        obj = User.objects.create_user(username=u, first_name=f, last_name=l, email=m, password=p)  # Corrected field names
        obj.save()
        return render(request, 'feed.html')
