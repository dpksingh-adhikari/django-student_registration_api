from django.contrib import admin
from django.urls import path
from classes.views import ClassCreateView
from Students.views import StudentDetailView,StudentListCreateView

urlpatterns = [
    path('class/',ClassCreateView.as_view()),
    path('studentregister/',StudentDetailView.as_view()),
    path('studentupdate/',StudentListCreateView.as_view()),
]
