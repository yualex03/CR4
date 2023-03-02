from rest_framework import serializers
from .models import TodoList, Todo

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        """
        Проверка, что задача имеет название и описание,
        а также что todo-список существует.
        """
        if not data.get('title'):
            raise serializers.ValidationError("Название задачи обязательно.")
        if not data.get('description'):
            raise serializers.ValidationError("Описание задачи обязательно.")
        if not TodoList.objects.filter(id=data.get('todo_list_id')).exists():
            raise serializers.ValidationError("Список задач с данным идентификатором не существует.")
        return data
