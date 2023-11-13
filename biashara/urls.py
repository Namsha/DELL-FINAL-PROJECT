from django.contrib import admin
from django.urls import path
from biashara import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('inner/', views.inner_page, name='inner'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointments, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('department/', views.departments, name='department'),
    path('addproducts/', views.addproducts, name='addproducts'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('pay/', views.pay, name='pay'),
    path('token/', views.token, name='token'),
    path('stk/', views.stk, name='stk'),
]
