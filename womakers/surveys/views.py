# https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/
# https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/

from django.views.generic import ListView, DetailView, CreateView
from .models import Question, Vote
from .forms import QuestionForm
from django.urls import reverse


class QuestionListView(ListView):
    model = Question

    def get_queryset(self):
        return Question.objects.filter(enabled=True)


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = context['question']
        context['form'] = QuestionForm(question=question)
        return context


class VoteCreateView(CreateView):
    model = Vote
    fields = ['option']

    def get_success_url(self):
        return reverse('question_detail', args=[self.object.option.question.pk])
