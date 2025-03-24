from django.db import models

class Student(models.Model):
    hall_ticket = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    telugu = models.IntegerField()
    hindi = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()

    @property
    def obtained_marks(self):
        return self.telugu + self.hindi + self.english + self.maths + self.science + self.social
    @property
    def total_marks(self):
        return (600)
    @property
    def percentage(self):
        return (self.obtained_marks / 600) * 100

    def __str__(self):
        return self.name
