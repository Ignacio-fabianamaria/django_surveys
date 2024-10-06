# https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/

from django.forms import ModelForm
from .models import Question
from django import forms


class QuestionForm(ModelForm):
    option = forms.ModelChoiceField(
        empty_label='',
        required=True,
        queryset=None,
        widget=forms.RadioSelect
        )

    class Meta:
        model = Question
        fields = ["option"]

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super().__init__(*args, **kwargs)
        self.fields['option'].queryset = question.option_set.all()

