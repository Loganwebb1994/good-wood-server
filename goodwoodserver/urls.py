from django.contrib import admin
from django.urls import path
from goodwoodapi.views import login_user, register_user, DropView, ProfileView
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter(trailing_slash=False)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'drops', DropView, 'drop')
router.register(r'profiles', ProfileView, 'profile')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]
