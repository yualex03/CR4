from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Todo(models.Model):
    name = models.CharField(max_length=255)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name