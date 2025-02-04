# Django imports
from django.db import models
from django.utils import timezone


# Create your models here.
# CI trigger
class Visit(models.Model):
    page: models.CharField = models.CharField(max_length=25)
    visit_time: models.DateTimeField = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Visited {self.page} on {self.visit_time}"
