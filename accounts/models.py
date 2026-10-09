# create your models here
from django.db import models
from django.contrib.auth.models import User


class FitnessProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    fitness_goal = models.CharField(max_length=50)

    weight_change = models.CharField(max_length=50)

    activity_level = models.CharField(max_length=50)

    equipment = models.CharField(max_length=50)

    workout_location = models.CharField(max_length=50)

    gym_frequency = models.CharField(max_length=50)

    home_workout_frequency = models.CharField(max_length=50)

    workout_duration = models.CharField(max_length=50)

    fitness_level = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
