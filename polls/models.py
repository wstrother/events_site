from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self) -> str:
        return self.question_text
    
    def get_vote_count(self) -> int:
        return sum([c.votes for c in self.choice_set.all()])

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.choice_text
    
    def get_vote_share(self) -> float:
        return round(100 * (self.votes / self.question.get_vote_count()), 2)
