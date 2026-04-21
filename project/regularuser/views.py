from django.shortcuts import render, loader , get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from jobs.models import Job
from .models import Applications 
from accounts.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def job_list(request):
    jobs = Job.objects.select_related('company').all()
    context = {
        'jobs': jobs,
    }
    template = loader.get_template('job_list.html')
    return HttpResponse(template.render(context, request))

def job_details(request, id):
  job = Job.objects.get(id=id)
  template = loader.get_template('job_details.html')
  context = {
    'job': job,
  }
  return HttpResponse(template.render(context, request))

@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        cv_link = request.POST.get('cv_link')
        user = request.user
        
        application = Applications.objects.create(
            userId=user,
            jobId=job,
            cvlink=cv_link
        )
        application.save()
        return redirect('applied_jobs')
    else:
        return render(request, 'job_details.html', {'job': job})

def applied_jobs(request):
    user = request.user
    applications = Applications.objects.filter(userId=user).select_related('jobId')
    context ={
        'user':user,
        'applications':applications
    }
    template = loader.get_template('applied_jobs.html')
    return HttpResponse(template.render(context,request))

def delete_application(request, application_id):
    application = get_object_or_404(Applications, pk=application_id)
    application.delete()
    return JsonResponse({'message': 'Application deleted successfully'})