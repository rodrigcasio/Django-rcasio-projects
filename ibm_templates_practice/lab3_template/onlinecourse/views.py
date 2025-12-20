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
#

# 1.
def popular_course_list(request):
    context = {}
    if request.method == 'GET':
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        context['course_list'] = course_list
        return render(request, 'onlinecourse/course_list.html', context) # 1.1

