from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all().order_by('-id')  #-id เรียงจากล่าสุด (มากไปน้อย)
    serializer_class = TodoSerializer

#CRUD     
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all().order_by('-id')  #-id เรียงจากล่าสุด (มากไปน้อย)
    serializer_class = TodoSerializer
    
