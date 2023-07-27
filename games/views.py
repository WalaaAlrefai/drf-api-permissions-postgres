from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView ,ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Game
from .serializers import GameSerializer

from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class GameListView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    # permission_classes = [IsOwnerOrReadOnly]

class GameDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]