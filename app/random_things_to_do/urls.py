from django.urls import path, include

from rest_framework.routers import DefaultRouter
from random_things_to_do import views

router = DefaultRouter()
router.register('random_things_to_do', views.RandomThingsToDoView, basename='RandomThingsToDo')

app_name='random_things_to_do'

urlpatterns = [
    path('', include(router.urls))
]