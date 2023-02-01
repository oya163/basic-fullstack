"""URL module for CompanyName"""
from django.urls import path

from thelab_backend import views

urlpatterns = [
    path('companyname/', views.CompanyNameDetail.as_view()),
]