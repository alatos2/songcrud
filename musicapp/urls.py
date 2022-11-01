from django.urls import path
from .views import SongDetailsView, SongView

urlpatterns = [
    path('songs/', SongView),
    path('details/<int:pk>/', SongDetailsView)
]