from django.db import models
from django.contrib.auth.models import User
from course.models import course

# Create your models here.

class Prompt(models.Model):
    WAITING_TO_VOTE = 0
    VOTING_OPEN = 1
    VOTING_COMPLETE = 2
    IS_ACCEPTING_VOTES_CHOICES = [
        (WAITING_TO_VOTE, 'Waiting to Vote'),
        (VOTING_OPEN, 'Voting Open'),
        (VOTING_COMPLETE, 'Voting Complete'),
    ]

    name = models.CharField(max_length=64)
    text = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    host_course = models.ForeignKey(course, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField()
    is_accepting_votes = models.IntegerField(default=0, choices=IS_ACCEPTING_VOTES_CHOICES)

class Response(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return "Response by:" + self.creator.username + self.text[0:300]

class FeudBallot(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    date_created = models.DateTimeField()
