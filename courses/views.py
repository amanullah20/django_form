from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.


def bangla(request):
    return render(request , 'course/course.html')




def show_form(request):
    frm= StudentRegistration(auto_id=True, label_suffix= ' ', initial={'email':'aiquest@mail.com'})
    frm.order_fields(field_order=['first_name','last_name','batch','email'])
    return render(request, 'course/form.html' , {'form':frm})