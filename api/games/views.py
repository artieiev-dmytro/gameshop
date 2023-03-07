from rest_framework import generics

from games.models import Game
from .serializers import GamesSerializer


class GamesAPIView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GamesSerializer
