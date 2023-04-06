from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer
from rest_framework.views import APIView
from .models import Todo

class TodoView(APIView):
    def get(self, request: Request) -> Response:
        todos = Todo.objects.all()
        data = {
            "results": []
        }
        for todo in todos:
            
            serializer = TodoSerializer(todo)
            data["results"].append(serializer.data)

        return Response(data, status=status.HTTP_200_OK)
    def post(self, request: Request) -> Response:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def add_todo(self,request:Request)->Response:
        if request.method =="POST":
            serializer = TodoSerializer(data=request.data)
            