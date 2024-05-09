from django.shortcuts import redirect, render
from .models import De
from .forms import DeForm

def home(request):

    ob=De.objects.all()
    return render(request,'home.html',{'obj':ob})

# Create your views here.
def add(request):
    
    if request.POST:
        name=request.POST.get('name')
        place=request.POST.get('place')
        number=request.POST.get('age')
        objects=De(name=name,place=place,age=number)
        objects.save()
        return redirect('home')
    return render(request,'add.html')

def delete(request,id):
    obj=De.objects.get(id=id)
    obj.delete()
    allobj=De.objects.all()
    return render(request,'home.html',{'obj':allobj})


def edit(request,id):
    boj=De.objects.get(id=id)
    if request.POST:
        name=request.POST.get('name')
        place=request.POST.get('place')
        no=request.POST.get('age')
        boj.name=name
        boj.place=place
        boj.age=no
        boj.save()
        return redirect('home')
    form=DeForm(instance=boj)
    return render(request,'form.html',{'form':form})
