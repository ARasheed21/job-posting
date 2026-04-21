from django.shortcuts import render, redirect, loader
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from jobs.models import Job

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User created'
            return redirect('login_view')
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminhome')
            elif user is not None and user.is_regular:
                login(request, user)
                return redirect('userhome')
            else:
                msg = 'Invalid Credentials'
        else:
            msg = 'Error Validating Form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def adminhome(request):
    return render(request, 'admin_home.html')

def userhome(request):
    return render(request, 'user_home.html')


def search_jobs(request):
    search_option = request.GET.get('search-options')
    search_keyword = request.GET.get('search-bar')
    
    if search_option and search_keyword:
        if search_option == 'job-title':
            jobs = Job.objects.filter(title__icontains=search_keyword)
        elif search_option == 'exp-years':
            jobs = Job.objects.filter(experience__icontains=search_keyword)
    else:
        jobs = Job.objects.all()
    
    job_list = []
    for job in jobs:
        job_list.append({
                'title': job.title,
                'company_name': job.company.name,
                'company_logo': job.company.logo,
                'location': job.location,
                'salary': job.salary,
                'status': job.status,
                'experience': job.experience,
                'id': job.id,
            })

    return JsonResponse({'jobs': job_list})

def job_details(request, id):
  job = Job.objects.get(id=id)
  template = loader.get_template('job_details.html')
  context = {
    'job': job,
  }
  return HttpResponse(template.render(context, request))
