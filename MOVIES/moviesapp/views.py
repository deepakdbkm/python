from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from moviesapp.forms import MovieForm
from moviesapp.models import movie


def demo(request):

    movies=movie.objects.all()
    context={'movielist':movies}
    return render(request,'index.html',context)
def detail(request,movie_id):
    movi=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movi':movi})
    return HttpResponse("this is movie no %s" % movie_id)
def add_movie(request):

    if request.method == "POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img=request.FILES['img']
        movi=movie(name=name,desc=desc,year=year,img=img)
        movi.save()
    return render(request,'add.html')
def update(request,id):
    movi=movie.objects.get(id=id)
    formm=MovieForm(request.POST or None,request.FILES, instance=movi)
    if formm.is_valid():
        formm.save()
        return redirect('/')
    return render(request,'edit.html',{'formm':formm,'movi':movi})


def delete (request,id):
    if request.method=='POST':
        movi=movie.objects.get(id=id)
        movi.delete()
        return redirect('/')
    return render(request,'delete.html')

