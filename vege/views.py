from django.shortcuts import render, redirect
from.models import *
from django.http import *
from django.conf import settings
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Sum
from .seed import generate_report_card


@login_required(login_url='/login')
def recepies(request):
    if request.method == 'POST':
        data = request.POST
        recepie_image = request.FILES.get('recepie_image')
        recepie_name = data['recepie_name']
        recepie_description = data['recepie_description']
        Recepie.objects.create(
            recepie_image=recepie_image,
            recepie_name=recepie_name,
            recepie_description=recepie_description
        )
        return redirect('recepies')
    
    queryset = Recepie.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(recepie_name__icontains=request.GET.get("search"))

    context = {'recepies': queryset}
    return render(request, "recepies.html",context)

@login_required(login_url='/login')
def delete_recepie(request, id):
    queryset = Recepie.objects.get(id=id)
    queryset.delete()
    recepie_image = queryset.recepie_image
    image_path = os.path.join(settings.MEDIA_ROOT, recepie_image.name)
    if os.path.exists(image_path):
        os.remove(image_path)
    return redirect('recepies')

@login_required(login_url='/login')
def update_recepie(request, id):
    queryset = Recepie.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        recepie_image = request.FILES.get('recepie_image')
        recepie_name = data['recepie_name']
        recepie_description = data['recepie_description']
        queryset.recepie_name=recepie_name
        queryset.recepie_description=recepie_description
        if recepie_image:
            queryset.recepie_image=recepie_image
        queryset.save()
        return redirect('recepies')
    context = {'recepies': queryset}
    return render(request,"update_recepies.html",context)


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect("/register")
        
        user = authenticate(username = username,password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login')
        else:
            login(request,user)
            return redirect("/recepies")
    
    return render(request , 'login.html')

def register(request):
    if request.method != "POST":
        return render(request , 'register.html')
    first_name=request.POST.get("first_name")
    last_name=request.POST.get("last_name")
    username=request.POST.get("username")
    password=request.POST.get("password")
    user=User.objects.filter(username=username)
    if user.exists():
        messages.error(request, "This user already exists.")
        return redirect("register")

    user=User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username
    )

    user.set_password(password)
    user.save()
    messages.info(request, "Account created Successfully")
    return redirect('register')

def logout_page(request):
    logout(request)
    return redirect('/login')

def get_students(request):
    queryset = Student.objects.all()
    ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks')
    print(ranks)
    for rank in ranks:
        print(rank.marks)
    if request.GET.get('search'):
        search=request.GET.get("search")
        queryset=queryset.filter(Q(student_name__icontains=search)|
                                 Q(department__department__icontains=search)|
                                 Q(student_id__student_id__icontains=search)|
                                  Q(student_email__icontains=search))
    paginator = Paginator(queryset, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request , 'report/students.html', {"queryset":page_obj})

def see_marks(request,student_id):
    # generate_report_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    print(queryset)
    total_marks= queryset.aggregate(total_marks=Sum('marks'))
    return render(request,'report/see_marks.html',{"queryset":queryset,'total_marks':total_marks})

