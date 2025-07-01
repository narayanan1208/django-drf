from rest_framework import serializers
from students.models import Student


# Serializers are used to convert complex query sets to dictionary for json representation.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
