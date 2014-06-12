from django.views.generic import TemplateView, FormView, UpdateView, View

# Create your views here.
class MainPageView(TemplateView):
  template_name='main/main.html'