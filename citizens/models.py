from django.db import models
from django.contrib.auth.models import AbstractUser

class Citizen(AbstractUser):
    age = models.PositiveIntegerField()
    occupation = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
