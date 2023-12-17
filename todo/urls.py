from django.urls import path
from todo.views import ToDoAPI 
from rest_framework.routers  import DefaultRouter
router = DefaultRouter()
router.register("todo", ToDoAPI, basename="users")


urlpatterns = []
urlpatterns+=router.urls
