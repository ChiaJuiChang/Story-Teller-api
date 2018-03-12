from django.shortcuts import render
from .models import Story,User,Message,Theme
from .serializers import StorySerializer,UserSerializer,MessageSerializer,ThemeSerializer
from rest_framework import viewsets
# Create your views here.

class StoryViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Story.objects.all()
	serializer_class = StorySerializer
	#pagination_class = None


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	#pagination_class = None


class MessageViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer
	#pagination_class = None

class ThemeViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Theme.objects.all()
	serializer_class = ThemeSerializer
	#pagination_class = None
