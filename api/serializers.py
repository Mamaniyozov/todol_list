from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.Serializer):
    task = serializers.CharField(max_length=100)
    description = serializers.CharField()
    completed = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    def create(self, validated_data):
        todo = Todo.objects.create(
            task=validated_data['task'],
            description=validated_data['description'],
            completed=validated_data['completed'],
        )
        return todo