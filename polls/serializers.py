from rest_framework import serializers
from .models import Student, Investor, Operation, University

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = '__all__'


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Investor
        fields = '__all__'

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Operation
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=University
        fields = '__all__'


