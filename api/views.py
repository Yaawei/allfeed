from rest_framework import generics
from accounts.models import LikedEntry
from django.contrib.auth.models import User
from .serializers import LikedEntrySerializer


class LikedEntryView(generics.ListAPIView):
    lookup_url_kwarg = 'username'
    serializer_class = LikedEntrySerializer

    def get_queryset(self):
        username = self.kwargs.get(self.lookup_url_kwarg)
        user = User.objects.get(username=username)
        return LikedEntry.objects.filter(user=user)
