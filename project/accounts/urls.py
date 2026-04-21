from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('userhome/', views.userhome, name='userhome'),
    path('search_jobs/', views.search_jobs, name='search_jobs'),
    path('details/<int:id>', views.job_details, name='job_details'),
]