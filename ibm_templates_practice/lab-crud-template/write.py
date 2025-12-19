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

def write_instructors():
    # Create User and add instructor
    user_john = User(first_name='John', last_name='Doe', dob=date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=30050)
    
    # Updating the user reference of instructor_john to be user_john
    instructor_john.user = user_john
    instructor_john.save()
    
    #django will automatically assing values 'first_name', 'last_name' and 'dob' to their parent user objects
    
    instructor_yan = Instructor(first_name='Yan', last_name='Luo', dob=date(1962, 7, 13), full_time=True, total_learners=30050)
    instructor_yan.save()

    instructor_joy = Instructor(first_name='Joy', last_name='Li', dob=date(1992, 1, 2), full_time=False, total_learners=10040)
    instructor_joy.save()

    instructor_peter = Instructor(first_name='Peter', last_name='Chen', dob=date(1982, 5, 2), full_time=True, total_learners=2002)
    instructor_peter.save()

    print("Instructor  objects all saved...")

def write_learners():
    # Adding learners
    # 1
    learner_james = Learner(first_name='James', last_name='Smith', dob=date(1982, 7, 9), occupation="data_scientist",
                            social_link='https://www.linkedin.com/james/')
    learner_james.save()
    # 2
    learner_mary = Learner(first_name='Mary', last_name='Smith', dob=date(1991, 6, 12), occupation='dba',
                           social_link='https://www.facebook.com/mary/')
    learner_mary.save()
    # 3
    learner_robert = Learner(first_name='Robert', last_name='Lee', dob=date(1999, 1, 2), occupation='student',
                             social_link='https://www.facebook.com/robert/')
    learner_robert.save()
    # 4
    learner_david = Learner(first_name='David', last_name='Smith', dob=date(1983, 7, 16), occupation='developer',
                            social_link='https://www.linkedin.com/david/')
    learner_david.save()
    #5
    learner_john = Learner(first_name='John', last_name='Smith', dob=date(1986, 3, 16), occupation='developer',
                           social_link='https://www.linkedin.com/john/')
    learner_john.save()
    #6
    learner_rodrig = Learner(first_name='Rodrig', last_name='Casio', dob=date(1999, 9, 7), occupation="student",
                             social_link='http://www.linkedin.com/rodrig')
    learner_rodrig.save()

    print("Learner objects all saved...")

def write_courses():
    # Add courses
    course_cloud_app = Course(name="Cloud Application Development with Database",
                            description="Develop and deploy application on cloud")
    course_cloud_app.save()

    course_python = Course(name="Introduction to Python", 
                        description="Learn core concepts of Python and obtain hands-on experience via capstone project")

    course_python.save()

    print("Course objects all saved...")


def write_lessons():
    lesson1 = Lesson(title="Lesson 1", content="Object-relational mapping project")
    lesson1.save()

    lesson2 = Lesson(title="Lesson 2", content="Django full stack project")
    lesson2.save()

    print("Lesson objects all saved...")

# to conveniently clean up database tables:
def clean_data():
    Enrrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()


# cleans any existing data first
clean_data()
write_courses()
write_instructors()
write_lessons()
write_learners()


