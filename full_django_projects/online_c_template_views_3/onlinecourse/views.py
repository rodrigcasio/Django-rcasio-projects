from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404

# 1. Add view to get the top 10 popular courses from models
# - 1.1 Create a context dictionay obj and append course_list into context
#    IMPORTANT: (next add the route path for popular_course_list view in urls.py)
#   onlinecourse/urls.py = path(route='', view=views.popular_course_list, name='popular_course_list'),
# 2. Create an enroll view to add one to the total_enrollment field
#   - view reads a course object based on the course_id argument
#   - if the course doesnt exist in database, it returns HTTP response with status code 404 not found error
#   - then it simply increases the total enrollment by one and updates the object 
#   - should always return an HttpResponseRedirect after succesfully dealing with POST data
# ... 

# 1.
def popular_course_list(request):
    context = {}
    if request.method == 'GET':
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        context['course_list'] = course_list
        return render(request, 'onlinecourse/course_list.html', context) # 1.1

# 2 
def enroll(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course.id)     # if it cannot be found

        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(reverse(viewname='onlinecourse:popular_course_list'))


