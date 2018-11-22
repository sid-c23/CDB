from django.contrib.auth.models import User, Group
from rest_framework import serializers
from club.models import Club

class UserSerializer(serializers.HyperlinkedModelSerializer):
	#clubs = serializers.HyperlinkedRelatedField(many=True, queryset=Club.objects.all())
	class Meta:
		model = User
		fields = ('id', 'url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')