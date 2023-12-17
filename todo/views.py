from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from todo.models import Task
from todo.serializers import TaskSerializer
# Create your views here.
class ToDoAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
