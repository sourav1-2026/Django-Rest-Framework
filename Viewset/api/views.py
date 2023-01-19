from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .Seriaalizer import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class studentViewSet(viewsets.ViewSet):
    def list(self,reuqest):
        print('List') 
        print ("Basename:", self.basename)
        print ("Action:", self.action)
        print ("Detail:", self.detail)
        print ("Suffix:", self. suffix)
        print ("Name:", self.name)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,reuqest,pk=None):
        id=pk
        if id is not None:
            stu=Student.ob.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
    
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data Updates'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        stu = Student. objects. get (id=id)
        serializer = StudentSerializer(stu, data=request.data,
        partial=True)
        if serializer. is_valid():
            serializer. save()
            return Response({'msg' : 'Partial Data Updated'})
        return Response(serializer.errors)
    def destroy(self, request, pk):
        id = pk
        stu = Student.objects. get(pk=id)
        stu.delete()
        return Response({'msg':'data Deleted'})



