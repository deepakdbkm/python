from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import place1


# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def detail(request):
    return HttpResponse("detailpage")
def thanks(request):
    return HttpResponse("thank you")
def demo(request):
    obj=place.objects.all()
    objc = place1.objects.all()

    return render(request,"index.html",{'result':obj,'results':objc})




def process1(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return render(request, "result.html", {'addition': add, 'substraction': sub, 'multiplication': mul,
      'division': div})


   #return render(request, "result.html", {"addition":res})


