from django.contrib import admin
from .models import ErrorNumber, Question, Solution, Work, WorkDetail

admin.site.register(ErrorNumber)
admin.site.register(Question)
admin.site.register(Solution)
admin.site.register(Work)
admin.site.register(WorkDetail)

