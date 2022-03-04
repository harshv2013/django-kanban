from rest_framework import serializers
from .models import Todo, Student

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('pk', 'name', 'email', 'document', 'phone', 'registrationDate')