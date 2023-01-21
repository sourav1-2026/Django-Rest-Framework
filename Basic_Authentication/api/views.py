from .models import Student
from .Seriaalizer import StudentSerializer
from rest_framework import viewsets

# now we are applying basic authentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # we want to apply authentication to this api
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

    #DEFINED  GLOBALLY IN SETTING


"""
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # we want to OVERRIDE THE GLOABAL AUTHETICATION
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[Allowany]

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # we want to apply authentication to this api
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

"""