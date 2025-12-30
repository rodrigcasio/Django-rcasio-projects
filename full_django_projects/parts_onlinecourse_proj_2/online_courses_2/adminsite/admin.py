from django.contrib import admin
from .models import Course, Instructor, Lesson

# 1. registering course and instructor models
# 2. Customize admin site Course 
# 3. Update the previous Course registration (adding 'CourseAdmin')
# 4. Customize fields for Instructor Model

# 5. Associate related objects on a single model managing page 
#   with defining `Inline` classes
#
#    5.1 Manage Lesson model together with Course model on a Course admin page.
#       - Adding a LessonInline class before CourseAdmin class
#    5.2 Update CourseAdmin class by adding 'inlines' list.
#(This adds the model of Lessons within Course Registration page (adding 5 models of Lessons that can be fill out))

# 5.1
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# 4., 5.2
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]

# 2,
class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']


# 1. 3. 4.
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
