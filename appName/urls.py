from django.urls import path

from .views import IndexView, QuestionView

app_name = 'appName'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('question/<int:error_number>', QuestionView.as_view(), name="question"),
]