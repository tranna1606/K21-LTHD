from rest_framework import serializers
from courses.models import Category, Course, Lesson, Tag, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields = '__all__'
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tag
        fields = ['id','name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =['id','name','image','created_date','updated_date']


class ItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = instance.image.url

        return rep


class LessonSerializer(ItemSerializer):
    class Meta:
        model= Lesson
        fields =['id','subject','image','created_data','updated_data']


class LessonDetailsSerializer(LessonSerializer):
    tags = TagSerializer(many=True)


    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content','tags']


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(data["password"])
        user.save()

        return  user
    class Meta:
       model =User
       fields =['id','first_name','last_name','email','username','password','avatar']

       extra_kwargs={
           'password':{
               'write_only':True
           }
       }
