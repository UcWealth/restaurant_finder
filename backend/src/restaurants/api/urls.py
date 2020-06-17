from django.urls import path
from .views import RestaurantListView, RestaurantDetailView

urlpatterns = [
    path('', RestaurantListView.as_view()),
    path('<pk>', RestaurantDetailView.as_view()),
]