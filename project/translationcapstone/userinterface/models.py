from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Post(models.Model):
    post = models.CharField(max_length=500)

class Translation(models.Model):
    orginal = models.CharField(max_length=500)
    polarity_original = models.FloatField()
    subjectivity_original = models.FloatField()
    polarity_google = models.FloatField()
    subjectivity_google = models.FloatField()
    target = models.CharField(max_length=500)
    polarity_target = models.FloatField()
    subjectivity_target = models.FloatField()
