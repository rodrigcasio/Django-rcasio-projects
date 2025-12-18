from django.db import models
from django.utils.timezone import now

# Defining Models

class User(models.Model):
    first_name = models.CharField(null = False, max_length = 30, default = 'john')
    last_name = models.CharField(null = False, max_length = 30, default = 'doe')
    dob = models.DateField(null = True)
    
    def __str__(self):
        return f" {self.first_name} {self.last_name}"

class Instructor(User): # inherit from User
    full_time = models.BooleanField(default = True)
    total_learners = models.IntegerField()

    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Is full time: {str(self.full_time)}, Total Learners: {str(self.total_learners)}"

class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    
    OCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin'),
    ]
    
    occupation = models.CharField(
        null = False,
        max_length = 20,
        choices = OCUPATION_CHOICES,
        default = STUDENT
    )
    
    social_link = models.URLField(max_length = 200)
    
    def __str__(self):
        return f"First name: {self.first_name}, Last name: {self.last_name}, Date of Birth: {self.dob}, Occupation: {self.occupation}, Social Link: {self.social_link}."


class Course(models.Model):
    name = models.CharField(null = False, max_length = 100, default = 'online course')
    description = models.CharField(max_length = 500)
    
    instructor = models.ManyToManyField(Instructor) # relationship with instructor
    learner = models.ManyToManyField(Learner, through = 'Enrrollment') 

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}."


class Lesson(models.Model):
    title = models.CharField(max_length = 200, default = "title")
    course = models.ForeignKey(Course, null = True, on_delete = models.CASCADE)
    content = models.TextField()


class Enrrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'

    COURS_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]

    learner = models.ForeignKey(Learner, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    data_enrolled = models.DateField(default = now)
    mode = models.CharField(max_length = 5, choices = COURS_MODES, default = AUDIT)


"""
User and Instructor models with One-to-One relationship
Course and Lesson models with One-To-Many relationship
Course and Instructor with Many-to-Many relationship
"""
