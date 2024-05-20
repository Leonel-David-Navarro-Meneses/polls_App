from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField()

    def __str__(self):
       return self.question_text

class Choise(models.Model):
    choice_text = models.CharField(max_length=100)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
       return self.choice_text