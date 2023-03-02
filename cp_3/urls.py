from django.urls import path
from todo_app.views import TodoListList, TodoListDetail, TodoListTodoList, TodoList, TodoDetail

urlpatterns = [
    path('api/todo-lists/', TodoListList.as_view()),
    path('api/todo-lists/<int:pk>/', TodoListDetail.as_view()),
    path('api/todo-lists/<int:pk>/todos/', TodoListTodoList.as_view()),
    path('api/todos/', TodoList.as_view()),
    path('api/todos/<int:pk>/', TodoDetail.as_view()),
]