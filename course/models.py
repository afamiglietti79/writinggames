from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class course(models.Model):
    name = models.CharField(max_length=256)
    secret_code = models.CharField(max_length=64)
    start_date = models.DateField()
    time_offered = models.TimeField()
    last_cleared = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name

class roll(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField()
