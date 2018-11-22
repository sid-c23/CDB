from .models import Club, Announcement
from .serializers import ClubSerializer, AnnouncementSerializer
from rest_framework import viewsets
# Create your views here.

class ClubViewSet(viewsets.ModelViewSet):
	queryset = Club.objects.all()
	serializer_class = ClubSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
	queryset = Announcement.objects.all()
	serializer_class = AnnouncementSerializer
