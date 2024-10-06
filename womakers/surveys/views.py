# https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/

from django.views.generic import ListView
from .models import Question


class QuestionListView(ListView):
    model = Question

    def get_queryset(self):
        return Question.objects.filter(enabled=True)
