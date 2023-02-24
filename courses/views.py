from django.shortcuts import render
from .forms import StudentRegistration
from courses.models import Student
from django.http import HttpResponseRedirect
from . models import Info

# Create your views here.


def bangla(request):
    return render(request , 'course/course.html')




def show_form(request):
    if request.method== 'POST':
        frm=StudentRegistration(request.POST)
        if frm.is_valid():
            fn=frm.cleaned_data['first_name']
            lname=frm.cleaned_data['last_name']
            bth=frm.cleaned_data['batch']
            eml=frm.cleaned_data['email']
            pas=frm.cleaned_data['password']
            txt=frm.cleaned_data['text']
            rpas=frm.cleaned_data['re_password']
            pay= frm.cleaned_data['payment']
            dj=frm.cleaned_data['django']
            
            djangoone=Info(first_name=fn,last_name=lname,batch=bth , email=eml ,password=pas,text=txt,re_password=rpas,payment = pay , django=dj)
            djangoone.save()
            return HttpResponseRedirect('/successfully/')
    else:
        frm= StudentRegistration(auto_id=True, label_suffix= ' ', initial={'email':'aiquest@mail.comg'})
        frm.order_fields(field_order=['first_name','last_name','batch','email','password','text'])
        return render(request, 'course/form.html' , {'form':frm})


def student_info(request):
    sdetails = Student.objects.all()
    return render(request,'course/std.html',{'std':sdetails})




def success(request):
    return render(request,'course/success.html')