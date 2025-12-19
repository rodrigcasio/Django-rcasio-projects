# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings')
from django.db import connection

# Ensures settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date

# 1. Find single instructor with first name 'Yan'
instructor_yan = Instructor.objects.get(first_name='Yan')
print(f"1. Find a single instructor with first name 'Yan' = {instructor_yan} ")
print('\n')

# 2. Find non-existing instructor with first name 'Andy'
try:
    instructor_andy = Instructor.objects.get(first_name='Andy')  
except Instructor.DoesNotExist:
    print(f"2. Try to find a non-existing instructor with first name 'Andy'")
    print(f"Instructor 'Andy' does not exist..")
    
print('\n')

# 3. Find all partime instructor
part_time_instructors = Instructor.objects.filter(full_time=False)
print(f"3. Find all part time instructors \
        {part_time_instructors}.")
print('\n')

# 4 Find all full time instructors with Firstname starts with 'y' and learners count is greater than 3000
"""
full_time_instructors = Instructor.objects.exclude(full_time=True).filter(total_learners__gt=30000). \
                        filter(first_name__startswith='Y')
print(f"4. Find all full time instructors with First name starts with 'Y' and learners count greater than 3000 \
        {full_time_instructors}.")
print('\n')
"""
# 5 same thing but with multiple parameters within filter
full_time_instructors = Instructor.objects.filter(full_time=True, total_learners__gt=30000, first_name__startswith='Y')
print(f" 4 & 5. Find all full time instructors with First name starts with 'Y' and learners count greater than 30000 \
        {full_time_instructors}.")


"""
OUTPUT:
((.venv) ) rodrig@rcasio-Archon lab-crud-template]$ python read_instructor.py

1. Find a single instructor with first name 'Yan' = First name: Yan, Last name: Luo, Is full time: True, Total Learners: 30050


2. Try to find a non-existing instructor with first name 'Andy'
Instructor 'Andy' does not exist..


3. Find all part time instructors       
    <QuerySet [<Instructor: First name: Joy, Last name: Li, Is full time: False, Total Learners: 10040>]>.


 4 & 5. Find all full time instructors with First name starts with 'Y' and learners count greater than 30000         
    <QuerySet [<Instructor: First name: Yan, Last name: Luo, Is full time: True, Total Learners: 30050>]>.

"""

