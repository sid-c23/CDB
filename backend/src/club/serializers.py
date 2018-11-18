from .models import Club, Announcement
from rest_framework import serializers

class ClubSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Club
		fields = ("name", "description", "members")
	
class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Announcement
		fields = ("club", "text", "author")