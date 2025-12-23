from django.contrib import admin
from .models import Course, Instructor, Lesson

## 4. Associate Related Models (defining Inline classes)
# then adding this to Course Admin class
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

## 2 Customize Admin site (adding 'CourseAdmin' within registers below):
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]

## 3. Customize fields for Instructor Model (adding 'InsructorAdmin' within register below)
class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']


# 1 register models with Admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)

