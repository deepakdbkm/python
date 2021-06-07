from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

# from todoapp.forms import todoform
from .forms import todoform
from .models import task
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
# from django.views.generic.detail import  DetailView



class tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'TASK1'
class detail(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'tak'
class tupdate(UpdateView):
    model = task
    template_name = 'update.html'

    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class tdelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')


def add(request):
    TASK1 = task.objects.all()
    if request.method=='POST':
         name=request.POST.get('name','')
         priority=request.POST.get('priority','')
         date=request.POST.get('date','')
         TASK=task(name=name,priority=priority,date=date)
         TASK.save()
         return redirect('/')
    return render(request,'home.html',{'TASK1':TASK1})
# def details(request):

    # return render(request,'details.html',)
def delete(request,taskid):
    task11=task.objects.get(id=taskid)
    if request.method=='POST':
        task11.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    TASK=task.objects.get(id=id)
    f=todoform(request.POST or None, instance=TASK)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'TASK':TASK})

