from django.urls import path
from . import views



urlpatterns = [

    path('', views.bangla),
    path('form/',views.show_form, name = 'sform'),
    path('s/', views.student_info , name= 'stdnt'),
    path('successfully/',views.success , name='success')
]