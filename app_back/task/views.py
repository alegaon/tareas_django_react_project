from rest_framework import viewsets
from .serializers import TaskSelializer
from .models import Task

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSelializer
    queryset = Task.objects.all()
