# models.py
from django.db import models

JOB_CHOICES = sorted([("fe", "Front-End Engineer"),
                      ("be", "Back-End Engineer"),
                      ("fs", "Full Stack Engineer"),
                      ("qa", "QA Engineer"),
                      ("se", "System Engineer"),
                      ("ot", "Other")])

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128, null=True)
    birthdate = models.DateField(null=True)
    job = models.CharField(choices=JOB_CHOICES, default="System Engineer", max_length=60)
    elo = models.IntegerField(default=1000)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    template = models.TextField()
    players = models.IntegerField()
    difficulty = models.FloatField()

    def __str__(self):
        return self.name


class Submission(models.Model):
    name = models.CharField(max_length=64)
    code = models.TextField()
    author = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='submissions', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    submissions = models.ManyToManyField(Submission, related_name='tournaments')
