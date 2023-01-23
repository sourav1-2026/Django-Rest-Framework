"""
In vies set you dont need to mainatain the url .you just have to make a router and register your class with the router and leave 
everything on me


"""
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter() # created a router object

# Now we have to register our view class with the router
# in this case it is studentViewSet
router.register('studentapi',views.StudentModelViewSet,basename='student')
#router.register('studentapi/<:int>',views.studentViewSet,basename='student')  router will take care of that url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
