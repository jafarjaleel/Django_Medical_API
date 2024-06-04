from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('list/', views.list_medicine, name='medicinelist'),
    path('add/', views.add_medicine,name='medicineadd'),
    path('edit/<int:medicine_id>', views.edit_medicine, name='medicineedit'),
    path('delete/<int:medicine_id>', views.delete_medicine, name='medicinedelete'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    

]
