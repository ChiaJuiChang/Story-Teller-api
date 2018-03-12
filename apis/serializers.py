from rest_framework import serializers
from .models import Message,Story,User,Theme

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = ('id','message_content','commenter','message_created_dt','like_counts')

class StorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Story
		fields = ('id','story_title','story_author','story_first_sentence','story_created_dt','message_counts','follow_counts','story_theme')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('user_id','user_password','user_name','user_picture','user_level')

class ThemeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Theme
		fields = '__all__'
