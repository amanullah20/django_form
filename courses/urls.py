from django.urls import path
from . import views



urlpatterns = [

    path('', views.bangla),
    path('form/',views.show_form, name = 'sform'),
]