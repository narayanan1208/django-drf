from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.studentsView),
    path("students/<int:pk>/", views.studentDetailView),
    # as_view() identifies it as class based views
    path("employees/", views.Employees.as_view()),
    path("employees/<int:pk>/", views.EmployeeDetail.as_view()),
]
