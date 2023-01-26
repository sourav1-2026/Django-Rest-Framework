from .models import Student
from .Seriaalizer import StudentSerializer
from rest_framework import viewsets

# now we are applying basic authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # we want to apply authentication to this api
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[IsAdminUser]
    #permission_classes=[IsAuthenticatedOrReadOnly]  # auth user has the ability to write but unauth user only have the ability to read.
    # it does not gIsAdminUserin page.
    # to enable login in browsable api we use built in url of django
    #permission_classes=[DjangoModelPermissions]  # it give  auth user to only read and if you want to add some functionality then add with the django admin oannel


"""
a) through admin pannel
b)generating token from DRf command
c) By exposing an API endpoint

"""