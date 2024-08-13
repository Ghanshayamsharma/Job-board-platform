from django.contrib import admin
from .models import JobListing, CandidateProfile, JobApplication, Company

admin.site.register(JobListing)
admin.site.register(CandidateProfile)
admin.site.register(JobApplication)
admin.site.register(Company)

