from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


class Student(models.Model):
    name = models.CharField(max_length=200)
    maths_score = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100), ])
    science_score = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100), ])
    history_score = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100), ])
    social_score = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100), ])

    def __unicode__(self):
        return self.name

