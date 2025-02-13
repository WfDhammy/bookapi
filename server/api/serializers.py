from rest_framework import serializers
from .models import Author, Course

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'firstname', 'lastname', 'othername', 'email', 'phone_number_1', 'phone_number_2', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="email", queryset=Author.objects.all())
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'author', 'created_at', 'full_name']
        read_only_fields = ['id', 'created_at']

    def get_full_name(self, obj):
        return f"{obj.author.firstname} {obj.author.lastname}"