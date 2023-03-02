from rest_framework import generics, filters
from .models import TodoList, Todo
from .serializers import TodoListSerializer, TodoSerializer

class TodoListList(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class TodoListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class TodoListTodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        todo_list_id = self.kwargs['pk']
        qs = Todo.objects.filter(todo_list_id=todo_list_id)
        status = self.request.query_params.get('status', None)
        if status is not None:
            qs = qs.filter(status=status)
        ordering = self.request.query_params.get('ordering', None)
        if ordering is not None:
            qs = qs.order_by(ordering)
        return qs

    def perform_create(self, serializer):
        todo_list_id = self.kwargs['pk']
        serializer.save(todo_list_id=todo_list_id)

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'completed_at']
    ordering = ['-created_at']

    def get_queryset(self):
        qs = Todo.objects.all()
        status = self.request.query_params.get('status', None)
        if status is not None:
            qs = qs.filter(status=status)
        ordering = self.request.query_params.get('ordering', None)
        if ordering is not None:
            qs = qs.order_by(ordering)
        return qs

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

