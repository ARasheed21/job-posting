from django.urls import path
from . import views
from .views import delete_job, edit_job

urlpatterns = [
    path('create/', views.add_job, name='add_job'),
    path('posted-jobs/', views.posted_jobs, name='posted_jobs'),
    path('delete/<int:job_id>/', delete_job, name='delete_job'),
    path('edit/<int:job_id>/', edit_job, name='edit_job'),
    
]

#path('', views.jobList, name='jobList'),