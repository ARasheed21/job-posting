from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .forms import JobForm
from .models import Job
from accounts.models import User


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            # Get the logged-in user
            current_user = request.user
            # Assign the logged-in user as the admin_id
            form.instance.admin_id = current_user
            # Get the company information of the logged-in user
            company_info = current_user.company_info
            # Assign the company information as the company
            form.instance.company = company_info
            # Save the form
            form.save()
            return redirect('posted_jobs')  # Redirect to the view that lists jobs
    else:
        form = JobForm()

    return render(request, 'add job phase_1.html', {'form': form, 'form_type' :'add'})



def posted_jobs(request):
    # Retrieve all jobs posted by the currently logged-in user
    user_jobs = Job.objects.filter(admin_id=request.user)
    return render(request, 'posted_jobs.html', {'user_jobs': user_jobs})

def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        job.delete()
        return redirect('posted_jobs')  # Redirect to the list of posted jobs
    return redirect('posted_jobs')



def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('posted_jobs')  # Redirect to the list of posted jobs
    else:
        form = JobForm(instance=job)
    return render(request, 'add job phase_1.html', {'form': form,'form_type':'edit'})

