from django import forms
from .models import JobApplication, CandidateProfile

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['status']

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['resume', 'bio', 'skills']
