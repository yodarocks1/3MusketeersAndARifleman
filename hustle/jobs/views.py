from django.shortcuts import render, redirect
from .forms import NewJobForm
from django.contrib import messages
from main.auth import user_passes_test, user_is_authenticated, user_in_group
from .models import Job


@user_is_authenticated()
@user_in_group("Customer")
def create_job_request(request):
    if request.method == "POST":
        form = NewJobForm(request.POST)
        errors = form.errors
        if form.is_valid():
            job = form.save()
            job.complete = False
            job.customer = request.user
            job.save()
            messages.success(request, "Job submitted successfully.")
            return redirect("jobs:view")
        messages.error(request, errors)
        messages.error(request, "There was invalid information in your job form. Please review and try again.")
    form = NewJobForm()
    return render(request=request, template_name='jobs/job_form.html', context={"create_job_form": form})


@user_is_authenticated()
def view(request):
    open_jobs = Job.objects.filter(customer=request.user, complete=False)
    completed_jobs = Job.objects.filter(customer=request.user, complete=True)
    return render(request=request, template_name="jobs/view_all.html", context={"open_jobs": open_jobs, "completed_jobs": completed_jobs})


@user_is_authenticated()
@user_in_group("Customer")
def update_job_request(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        return redirect("jobs:view")
    if not job.request_from_owner(request):
        return redirect("jobs:view")
    if request.method == "POST":
        form = NewJobForm(request.POST)
        errors = form.errors
        if form.is_valid():
            job = form.instance
            job.complete = False
            job.customer = request.user
            job.id = job_id
            job.save()
            messages.success(request, "Job submitted successfully.")
            return redirect("jobs:view")
        messages.error(request, errors)
        messages.error(request, "There was invalid information in your job form. Please review and try again.")
    form = NewJobForm(instance=job)
    return render(request=request, template_name='jobs/edit_job_form.html', context={"create_job_form": form})


@user_is_authenticated()
def view_job(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        return redirect("jobs:view")
    return render(request=request, template_name='jobs/view_job.html', context={"job": job})

@user_is_authenticated()
def view_all_jobs(request):
    jobs = Job.objects.all()
    return render(request=request, template_name='jobs/view_every_job.html', context={"jobs": jobs})
