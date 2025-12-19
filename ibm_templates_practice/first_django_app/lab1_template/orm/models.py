from django.db import models

# This is the first model ORM helps in creating this into a Database Table named User (Model)

class User(models.Model):
    first_name = models.CharField(null = False, max_length = 30, default = 'john')
    last_name = models.CharField(null = False, max_length = 30, default = 'doe')
    dob = models.CharField(null = True)
