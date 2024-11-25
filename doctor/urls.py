from django.urls import path
from . import views

app_name= 'doctors'
urlpatterns = [
    path('',views.home,name="home"),
    path('create/',views.show_forms,name="create"),
    path('show/',views.doctors_list,name="show"),
    path('success/',views.success_message,name="success_message"),
    path('error',views.error_page,name="error_page"),
    path('show/<int:pk>/',views.doctor_show_detail,name="showdetail"),
    path('update/<int:pk>/',views.doctor_edit,name="edit"),
    path('delete/<int:pk>/',views.doctor_delete,name="delete"),
    path('forms/',views.show_forms,name="forms"),
  
]