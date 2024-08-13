from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/<int:pk>/apply/', views.apply_for_job, name='apply_for_job'),
    path('profile/create/', views.candidate_profile, name='candidate_profile'),
]
