from rest_framework import serializers
from courses.models import Category,Course

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image']=instance.image.url
        return rep
    class Meta:
        model = Course
        fields =['id','name','image','created_date','updated_date']