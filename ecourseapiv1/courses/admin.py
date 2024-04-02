from django.contrib import admin
from django.utils.html import mark_safe
from courses.models import Category, Course, Lesson, Like, Comment, Tag, User
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.
class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:

        model = Course
        fields = '__all__'


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name', 'description']
    list_filter = ['id', 'created_date', 'name']
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, instance):
        if instance:
            return mark_safe(f"<img width ='120' src='static/{instance.image.name}' />")


class Media:
    css = {
        'all': ('/static/css/style.css')
    }


admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(User)




