from rest_framework.response import Response
from rest_framework import status
from .models import Author, Course
from .serializers import AuthorSerializer, CourseSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view()
def main(request):
    return Response({"message": "Hello, world!", "status": status.HTTP_200_OK})


@api_view()
def authors(request):
    obj = Author.objects.all()
    serializer = AuthorSerializer(obj, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def get_author(request, id):
    obj = get_object_or_404(Author, id=id)
    serializer = AuthorSerializer(obj)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def delete_author(request, id):
    obj = get_object_or_404(Author, id=id)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def update_author(request, id):
    obj = get_object_or_404(Author, id=id)
    serializer = AuthorSerializer(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view()
def courses(request):
    obj = Course.objects.all()
    serializer = CourseSerializer(obj, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def get_course(request, id):
    obj = get_object_or_404(Course, id=id)
    serializer = CourseSerializer(obj)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def delete_course(request, id):
    obj = get_object_or_404(Course, id=id)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def update_course(request, id):
    obj = get_object_or_404(Course, id=id)
    serializer = CourseSerializer(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)