from django.test import TestCase
from ..models import Question, Option
from django.urls import reverse
from ..forms import QuestionForm


# import pdb; pdb.set_trace()


class QuestionDetailViewTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(text="Qual sua cor favorita?")
        self.option_1 = Option.objects.create(question=self.question, text='Azul')
        self.option_2 = Option.objects.create(question=self.question, text='Verde')

    def test_detailView_url_accessible_by_path(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_detailView_url_accessible_by_name(self):
        response = self.client.get(reverse('question_detail', args=[self.question.pk]))
        self.assertEqual(response.status_code, 200)

    def test_detailView_uses_correct_template(self):
        response = self.client.get(reverse('question_detail', args=[self.question.pk]))
        self.assertTemplateUsed(response, 'surveys/question_detail.html')

    def test_detailView_context_contains_question(self):
        response = self.client.get(reverse('question_detail', args=[self.question.pk]))
        self.assertEqual(response.context['question'], self.question)

    def test_detailView_context_contains_question_form(self):
        response = self.client.get(reverse('question_detail', args=[self.question.pk]))
        form = response.context['form']
        self.assertIsInstance(form, QuestionForm)

    def test_detailView_options_is_being_displaying_in_template(self):
        response = self.client.get(reverse('question_detail', args=[self.question.pk]))
        self.assertContains(response, self.option_1.text)
        self.assertContains(response, self.option_2.text)

    def test_detailView_title_is_being_displaying_in_template(self):
        response = self.client.get(reverse('question_detail', args=[self.question.pk]))
        self.assertContains(response, self.question.text)

