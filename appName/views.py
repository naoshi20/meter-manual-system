from django.views.generic import TemplateView, ListView
from django.core import serializers
from django.shortcuts import redirect
from .models import ErrorNumber, Question, Solution, Work, WorkDetail

class IndexView(ListView):
    template_name = 'appName/index.html'
    model = ErrorNumber

class QuestionView(TemplateView):
    template_name = "appName/question.html"
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        questions = Question.objects.filter(error_number=self.kwargs['error_number'])
        solutions = Solution.objects.filter(error_number=self.kwargs['error_number'])
        #qustion = Question.objects.get(question_id=error_number)
        ctx['questions'] = questions
        ctx['solutions'] = solutions
        return ctx

    def post(self, request, **kwargs):
        print(request.POST)
        return redirect('appName:index')