from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer, InvestorSerializer, OperationSerializer, UniversitySerializer
from .models import Student, Investor, Operation, University

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class StudentListView(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentDetailView(generics.RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentEdit(generics.RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentCreate(generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class InvestorListView(generics.ListAPIView):
    queryset=Investor
    serializer_class=InvestorSerializer

class InvestorDetailView(generics.RetrieveAPIView):
    queryset=Investor.objects.all()
    serializer_class=InvestorSerializer

class InvestorEdit(generics.RetrieveUpdateAPIView):
    queryset=Investor.objects.all()
    serializer_class=InvestorSerializer

class InvestorCreate(generics.CreateAPIView):
    queryset=Investor.objects.all()
    serializer_class=InvestorSerializer

class OperationListView(generics.ListAPIView):
    queryset=Operation.objects.all()
    serializer_class=OperationSerializer



# class OperationFilter(generics.ListAPIView):
#     queryset=Operation.objects.all()
#     serializer_class=OperationSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['University.title', 'Student.type_of_student']





