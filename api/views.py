# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import mixins, generics

# Function-based views


@api_view(["GET", "POST"])
def studentsView(request):
    if request.method == "GET":
        # Get all data from the Student table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Class-based views provide more structured and organized way to handle requests using OOPs.
# eg: get(), post(), put(), delete() etc.
# This ensured code reusablitiy.
# It does not need api decorators.

"""
class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            return employee
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


# Mixins are reusable code classes in object-oriented programming that provide specific functionalities.
# In Django REST framework, mixins are used to add common functionality to views.
# There are 5 types of mixins in Django.
# They are ListModelMixin, CreateModelMixin, RetriewModelMixin, UpdateModelMixin, DestroyModelMixin.
# These mixins use their build-in methods.
# ListModelMixin - list(); CreateModelMixin - create(); RetriewModelMixin - retrieve()
# UpdateModelMixin - update(); DestroyModelMixin - destroy();
# eg: create ModelName(mixins, generics.GenericAPIView)

"""
class Employees(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class EmployeeDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
"""

# Generic API View acts as a foundational class for building most API views.
# It provides essential functionalities for handling incoming HTTP requests
# such as get, post, put and delete. It also structures outgoing responses.

# Generics are pre-build view classes and mixins that encapsulates common API functionalities
# like creating, reading, updating and deleting without the need to write boilerplate code.
# There are 5 types of generic views in Django REST framework.
# They are ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView.
# There are combinations of these generic views such as
# ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView.


class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"
