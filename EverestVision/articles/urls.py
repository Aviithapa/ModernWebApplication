from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login/",views.login,name="login.url"),
    path("AdminDashBoard/",views.AdminDashBoard),
    path("AdminDashBoard/EmployeeRegistrations",views.AdminDashBoard),
    path("edit/<int:id>",views.edit),
    path("CustomerRegistrations",views.CustomerRegistrations),
    path("contact_form_submission",views.contact_form_submission),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('response/<int:id>',views.response),
    path('customerlogin/<int:id>',views.customerlogin),
]
