from django.shortcuts import render
from rest_framework import viewsets,generics
from courses import serializers,pagination
from courses.models import Category,Course
# Create your views here.

class CategoryViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class =serializers.CategorySerializer

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = pagination.CoursePaginator

    def get_queryset(self):
        queryset= self.queryset
        q = self.request.query_params.get('q')

        if q:
            queryset =queryset.filter(name__icontains= q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queryset = queryset.filter(category_id= cate_id)

        return queryset

