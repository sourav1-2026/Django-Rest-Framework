from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class meta:
        model=Student
        fields=['id','name','city','roll']