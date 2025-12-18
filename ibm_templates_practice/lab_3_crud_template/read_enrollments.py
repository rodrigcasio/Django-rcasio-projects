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

# 2 creating query related 'course', 'Learner' and 'User' Objects.

"""
Queries:
1. Get the user information about learner David
2. Get learner David information from user
3. Get all learners for Introduction to Python course
4. Check the occupation list for the courses taught by instructor Yan
5. Check which courses the developer learners are enrolled in Aug, 2020
"""

learner_david = Learner.objects.get(first_name='David')
print(f"1. Get the user information about learner 'David':\n {learner_david}\n")

user_david = User.objects.get(first_name='David')
print(f"Get learner David information from user\n {user_david}\n")

course = Course.objects.get(name='Introduction to Python')
learners = course.learners.all()
print(f"3. Get all learners for Introduction to Python course:\n {learners}\n")

courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print(f"4. Check the occupation list for the courses taught by instructor Yan:\n {occupation_list}\n")

enrollments = Enrollment.objects.filter(date_enrolled__month=8,
                                        date_enrolled__year=2020,
                                        learner__occupation='developer')
courses_for_developers = set()
for enrollment in enrollments:
    course = enrollment.course
    courses_for_developers.add(course.name)
print(f"5. Check which courses the developer learners are enrolled in Aug, 2020:\n {courses_for_developers}\n")

"""
*queries output expected*:

((.venv) ) rodrig@rcasio-Archon lab_3_crud_template]$ python read_enrollments.py
1. Get the user information about learner 'David':
 First name: David, Last name: Smith, Date of Birth: 1983-07-16, Occupation: developer, Social Link: https://www.linkedin.com/david/.

Get learner David information from user
  David Smith

3. Get all learners for Introduction to Python course:
 <QuerySet [<Learner: First name: Robert, Last name: Lee, Date of Birth: 1999-01-02, Occupation: student, Social Link: https://www.facebook.com/robert/.>]>

4. Check the occupation list for the courses taught by instructor Yan:
 {'dba', 'student', 'developer', 'data_scientist'}

5. Check which courses the developer learners are enrolled in Aug, 2020:
 {'Cloud Application Development with Database'}

"""
