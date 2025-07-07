from django.urls import path, include
from . import views
from jwt_auth_demo.views import RegisterView, LoginView, UserView, LogoutView
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
    path("blogs/", views.BlogsView.as_view()),
    path("comments/", views.CommentsView.as_view()),
    path("blogs/<int:pk>", views.BlogsDetailView.as_view()),
    path("comments/<int:pk>", views.CommentsDetailView.as_view()),
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("user/", UserView.as_view()),
    path("logout/", LogoutView.as_view()),
]
