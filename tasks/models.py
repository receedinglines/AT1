from django.db import models

class Question(models.Model):
    text = models.TextField(verbose_name="Question Text")

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name="Answer Text")
    is_correct = models.BooleanField(default=False, verbose_name="Is this the correct answer?")

    def __str__(self):
        return f"{self.text} ({'correct' if self.is_correct else 'incorrect'})"
