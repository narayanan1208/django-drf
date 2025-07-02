from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Registering the router with the viewset
# basename is used in case of viewsets.ViewSet
# If using ModelViewSet, it is not required
# as it automatically generates the basename from the queryset.
router.register("employees", views.EmployeeViewSet, basename="employee")

urlpatterns = [
    path("students/", views.studentsView),
    path("students/<int:pk>/", views.studentDetailView),
    # as_view() identifies it as class based views
    # path("employees/", views.Employees.as_view()),
    # path("employees/<int:pk>/", views.EmployeeDetail.as_view()),
    path("", include(router.urls)),  # Include the router's URLs
]
