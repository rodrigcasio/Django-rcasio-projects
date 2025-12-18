# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from related_objects.models import *
from datetime import date

# querying objects spanning relationships
"""
1. Get courses taught by Instructor Yan, via both forward (explicit) and backward (implicit) access
2. Get the instructors of Cloud app dev course
3. Check the occupations of the courses taught by instructor Yan
"""

courses = Course.objects.filter(instructors__first_name='Yan')
print(f"1. Get courses taught by Instructor 'Yan', forward:\n{courses}\n")

instructor_yan = Instructor.objects.get(first_name='Yan')
print(f"1.2. Get courses taught by Instructor 'Yan', backward = \n{instructor_yan.course_set.all()}.\n")

cloud_instructors = Instructor.objects.filter(course__name__contains='Cloud')
print(f"2. Get the instructors of Cloud app dev course:\n {cloud_instructors}\n")

courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print(f"3. Check the occupations of the courses taught by instructor 'Yan'\n {occupation_list}\n")

"""
Queries output expected:

((.venv) ) rodrig@rcasio-Archon lab_3_crud_template]$ python read_course_instructors.py
1. Get courses taught by Instructor 'Yan', forward:
<QuerySet [<Course: Name: Cloud Application Development with Database, Description: Develop and deploy application on cloud.>]>

1.2. Get courses taught by Instructor 'Yan', backward =
<QuerySet [<Course: Name: Cloud Application Development with Database, Description: Develop and deploy application on cloud.>]>.

2. Get the instructors of Cloud app dev course:
 <QuerySet [<Instructor: First name: Yan, Last name: Luo, Is full time: True, Total Learners: 30050>, <Instructor: First name: Joy, Last name: Li, Is full time: False, Total Learners: 10040>]>

3. Check the occupations of the courses taught by instructor 'Yan'
 {'data_scientist', 'developer', 'student', 'dba'}

"""



