from .models import Student
from .Seriaalizer import StudentSerializer
from rest_framework import viewsets

# now we are applying basic authentication
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # jwt access token where divided into three parts 
    # header : alogorithm and token type
    # payload: Data
    # verify signature
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]









    #authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]

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