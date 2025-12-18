# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings')
from django.db import connection

# Ensures settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from related_objects.models import *
from datetime import date

def write_instructors():
    # create the instructor directly Django will handle creating the undelying User
    instructor_john = Instructor(first_name='John', last_name='Doe', dob=date(1962, 7, 16), full_time=True, total_learners=30050)
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

def populate_course_instructor_relationships():
    # Get related instructors
    instructor_yan = Instructor.objects.get(first_name='Yan')
    instructor_joy = Instructor.objects.get(first_name='Joy')
    instructor_peter = Instructor.objects.get(first_name='Peter')

    # Get related courses
    course_cloud_app = Course.objects.get(name__contains='Cloud')
    course_python = Course.objects.get(name__contains='Python')

    # Add instructors to courses
    course_cloud_app.instructors.add(instructor_yan)
    course_cloud_app.instructors.add(instructor_joy)
    course_python.instructors.add(instructor_peter)
    
    print("Course-instructor relationships saved... ")

def populate_course_enrollment_relationships():

    # Get related courses
    course_cloud_app = Course.objects.get(name__contains='Cloud')
    course_python = Course.objects.get(name__contains='Python')

    # Get related learners
    learner_james = Learner.objects.get(first_name='James')
    learner_mary = Learner.objects.get(first_name='Mary')
    learner_david = Learner.objects.get(first_name='David')
    learner_john = Learner.objects.get(first_name='John')
    learner_robert = Learner.objects.get(first_name='Robert')
    learner_rodrig = Learner.objects.get(first_name='Rodrig')

    # Add enrollments
    james_cloud = Enrollment.objects.create(learner=learner_james, date_enrolled=date(2020, 8, 1),
                                            course=course_cloud_app, mode='audit')
    james_cloud.save()
    mary_cloud = Enrollment.objects.create(learner=learner_mary, date_enrolled=date(2020, 8, 2),
                                         course=course_cloud_app, mode='honor')
    mary_cloud.save()
    david_cloud = Enrollment.objects.create(learner=learner_david, date_enrolled=date(2020, 8, 5),
                                            course=course_cloud_app, mode='honor')
    david_cloud.save()
    john_cloud = Enrollment.objects.create(learner=learner_john, date_enrolled=date(2020, 8, 5),
                                           course=course_cloud_app, mode='audit')
    john_cloud.save()
    robert_python = Enrollment.objects.create(learner=learner_robert, date_enrolled=date(2020, 9, 2),
                                              course=course_python, mode='honor')
    robert_python.save()
    rodrig_cloud = Enrollment.objects.create(learner=learner_rodrig, date_enrolled=date(2025, 12, 16),
                                               course=course_cloud_app, mode='honor')
    rodrig_cloud.save()

    print("Course-learner relationships saved... ")

# -------- DELETE ALL DATA  Best practice example-------
def clean_data():
    # 1. Delete the "Links" (Middle-man tables)
    Enrollment.objects.all().delete()
    
    # 2. Delete the "Dependents" (Tables that need a course to exist)
    Lesson.objects.all().delete()

    # 3. Delete the "Main Entities"
    Course.objects.all().delete()
    
    # 4. Delete the "Top Level"
    # (Deleting User automatically deletes Learners and Instructors)
    User.objects.all().delete()
# --------------------------------


# --- CALLING FUNCTIONS 
# cleans any existing data first
clean_data()
# write data
write_courses()
write_instructors()
write_lessons()
write_learners()
# Populate relationships
populate_course_instructor_relationships()
populate_course_enrollment_relationships()


"""
checking database within PostgreSQL linux
psql -U lab_3_user -d lab_3_db
SELECT * FROM related_objects_user;
"""
