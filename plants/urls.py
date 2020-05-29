from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
router.register('rooms', views.RoomViewSet, basename='room')
router.register('plants', views.PlantViewSet, basename='plant')
router.register('userplants', views.UserPlantViewSet, basename='userplant')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', views.ProfileRetrieveView.as_view(), name='profile'),
]
