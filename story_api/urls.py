"""story_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from apis import views


router = routers.DefaultRouter()
router.register(r'story',views.StoryViewSet)
router.register(r'user',views.UserViewSet)
router.register(r'message',views.MessageViewSet)
router.register(r'theme',views.ThemeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
]
