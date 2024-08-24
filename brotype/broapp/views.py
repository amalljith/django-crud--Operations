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
        position=request.POST.get('position')
        number=request.POST.get('age')
        mobile=request.POST.get('mobile')
        objects=De(name=name,place=place,age=number,mobile=mobile,position=position)
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
        position=request.POST.get('position')
        no=request.POST.get('age')
        mobile=request.POST.get('mobile')
        boj.name=name
        boj.place=place
        boj.position=position
        boj.age=no
        boj.mobile=mobile
        boj.save()
        return redirect('home')
    form=DeForm(instance=boj)
    return render(request,'form.html',{'form':form})
