from django.urls import path
from . import views


urlpatterns = [
    path('list', views.job_list, name='job_list'),
    path('details/<int:id>', views.job_details, name='job_details'),
    path('appliedJobs',views.applied_jobs,name='applied_jobs'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('delete_application/<int:application_id>/', views.delete_application, name='delete_application')
]

