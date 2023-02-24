from django.contrib import admin
from .models import Student , Info
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
       list_display=('id', 'student_id', 'student_name','student_email','batch','course')
 
#admin.site.register(Student , StudentAdmin)

class InfoAdmin(admin.ModelAdmin):
       list_display = ('first_name','last_name','email','batch','password','payment','text')


admin.site.register(Info,InfoAdmin)       