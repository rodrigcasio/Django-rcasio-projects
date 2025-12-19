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

# find students with last name "Smith"
smith_learner = Learner.objects.filter(last_name='Smith')
print(f"1. Find learner with last name 'Smith': {smith_learner}")
print('\n')

# Order by bod descending, and select the first dob two objects
learners = Learner.objects.order_by('-dob')[0:2]
print(f"2. Find top two yongest learners: {learners}")

"""
OUTPUT:
((.venv) ) rodrig@rcasio-Archon lab-crud-template]$ python read_learners.py
1. Find learner with last name 'Smith': 
<QuerySet [<Learner: First name: James, Last name: Smith, Date of Birth: 1982-07-09, Occupation: data_scientist, Social Link: https://www.linkedin.com/james/.>, <Learner: First name: Mary, Last name: Smith, Date of Birth: 1991-06-12, Occupation: dba, Social Link: https://www.facebook.com/mary/.>, 
          <Learner: First name: David, Last name: Smith, Date of Birth: 1983-07-16, Occupation: developer, Social Link: https://www.linkedin.com/david/.>, 
          <Learner: First name: John, Last name: Smith, Date of Birth: 1986-03-16, Occupation: developer, Social Link: https://www.linkedin.com/john/.>]>


2. Find top two yongest learners: 
<QuerySet [<Learner: First name: Rodrig, Last name: Casio, Date of Birth: 1999-09-07, Occupation: student, Social Link: http://www.linkedin.com/rodrig.>, 
            <Learner: First name: Robert, Last name: Lee, Date of Birth: 1999-01-02, Occupation: student, Social Link: https://www.facebook.com/robert/.>]>

"""

