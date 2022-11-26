from django.db import models

class Solution(models.Model):
        solution_content = models.TextField()

        def __str__(self):
                return self.solution_content

class Question(models.Model):
        question_text = models.TextField()
        next_question_when_yes = models.IntegerField(blank=True, null=True)
        next_question_when_no = models.IntegerField(blank=True, null=True)
        solution_when_yes = models.IntegerField(blank=True, null=True)
        solution_when_no = models.IntegerField(blank=True, null=True)

        def __str__(self):
                return self.question_text

class ErrorNumber(models.Model):
        error_number = models.IntegerField(null=False)
        next_question = models.ForeignKey(Question, on_delete=models.CASCADE)

        def __str__(self):
                return str(self.error_number)

class Work(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        worker = models.CharField(max_length=400)
        error_number = models.IntegerField(null=False)
        solution = models.ForeignKey(ErrorNumber, on_delete=models.CASCADE)

        def __str__(self):
                return self.worker

class WorkDetail(models.Model):
        work_order = models.IntegerField(null=False)
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        answer = models.CharField(max_length=400)
        work = models.ForeignKey(Work, on_delete=models.CASCADE)

        def __str__(self):
                return str(self.work_order)