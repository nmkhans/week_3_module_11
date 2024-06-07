from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name = "meals"),
  path("meal-detail/<int:id>/", views.mealDetail, name="meal-detail")   
]
