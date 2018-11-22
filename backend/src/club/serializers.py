from .models import Club, Announcement
from rest_framework import serializers
from django.contrib.auth.models import User
class ClubSerializer(serializers.HyperlinkedModelSerializer):
	members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
	class Meta:
		model = Club
		fields = ('id', "url", "name", "description", "members")
	
class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Announcement
		fields = ('id', "url", "club", "text", "author")