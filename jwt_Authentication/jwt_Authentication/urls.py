from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import obtain_auth_token
#from api.Custome_auth import CustomauthToken


# Now we have to configure JWT in url.py
# import access view,refresh view,verify view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

# TokenObtainPairView this class will give us access token and refresh token

router=DefaultRouter()
router.register('studenapi',views.StudentModelViewSet,basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
    #path('gettoken/',obtain_auth_token),
    #path('gettoken/',CustomauthToken.as_view()),
]
