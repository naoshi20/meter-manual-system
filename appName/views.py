from django.views.generic import TemplateView, ListView
from .models import ErrorNumber, Question, Solution, Work, WorkDetail

class IndexView(ListView):
    template_name = 'appName/index.html'
    model = ErrorNumber

class AboutView(TemplateView):
    template_name = "appName/about.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["skills"] = [
            "Python",
            "C++",
            "Javascript",
            "Rust",
            "Ruby",
            "PHP"
        ]
        ctxt["num_services"] = 1234567
        return ctxt