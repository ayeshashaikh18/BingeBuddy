from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("step1/", views.step1, name="step1"),
    path("step2/", views.step2, name="step2"),
    path("step3/", views.step3, name="step3"),
    path("step4/", views.step4, name="step4"),
    path("step5/", views.step5, name="step5"),
    path("results/", views.results, name="results"),
]