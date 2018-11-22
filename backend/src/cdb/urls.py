"""cdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cdb import views
from club import views as clubviews
from rest_framework.authtoken import views as authviews

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'clubs', clubviews.ClubViewSet)
router.register(r'announcements', clubviews.AnnouncementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
		path('api-auth/', include('rest_framework.urls')),
		path('api/', include(router.urls)),
		path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),
		path('rest-auth/', include('rest_auth.urls')),
		path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
