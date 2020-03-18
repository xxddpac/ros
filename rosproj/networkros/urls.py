from rest_framework import routers
from . import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'networkros'
router = routers.DefaultRouter()


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'login', views.Login.as_view()),
    # path(r'home', views.Home.as_view()),
    path(r'device', views.Device.as_view()),

]
