from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobListing, CandidateProfile, JobApplication
from .forms import JobApplicationForm

def job_list(request):
    jobs = JobListing.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(JobListing, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(JobListing, pk=pk)
    candidate_profile = CandidateProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_listing = job
            application.candidate = candidate_profile
            application.save()
            return render(request, 'jobs/application_success.html')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})

@login_required
def candidate_profile(request):
    profile = CandidateProfile.objects.get(user=request.user)
    return render(request, 'jobs/candidate_profile.html', {'profile': profile})

