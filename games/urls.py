from django.urls import path
from .views import GameListView, GameDetailView

urlpatterns = [
    path('', GameListView.as_view(), name = 'games_list'),
    path('<int:pk>/', GameDetailView.as_view(), name = 'games_detail'),
]