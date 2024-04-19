from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    urll = models.URLField()
    type = models.IntegerField()
    generated = models.BooleanField(default=False)
    question1 = models.IntegerField(null=True)
    question2 = models.IntegerField(null=True)
    question3 = models.IntegerField(null=True)
    question4 = models.IntegerField(null=True)
    question5 = models.IntegerField(null=True)
    grade = models.BooleanField(default=0)
    def __str__(self):
        return f"Image #{self.id}"