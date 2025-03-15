from rest_framework.serializers import ModelSerializer
from .models import Category, Course, Lesson, Tag

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'created_date', 'category', 'pre_course']