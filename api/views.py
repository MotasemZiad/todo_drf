from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def api_overview(request):

    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<int:id>/',
        'Create': 'task-create/',
        'Update': 'task-update/<int:id>/',
        'Delete': 'task-delete/<int:id>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response("Task deleted Successfully!")
