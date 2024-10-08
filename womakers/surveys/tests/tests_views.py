from django.test import TestCase
from ..models import Question
from django.urls import reverse


# import pdb; pdb.set_trace()


class QuestionListViewTestCase(TestCase):
    def setUp(self):
        self.question1 = Question.objects.create(text="Pergunta 1")
        self.question2 = Question.objects.create(text="Pergunta 1")
        self.question3 = Question.objects.create(text="Pergunta 1", enabled=False)

    def test_view_url_accessible_by_path(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('question_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('question_list'))
        self.assertTemplateUsed(response, 'surveys/question_list.html')

    def test_view_only_enabled_questions(self):
        response = self.client.get(reverse('question_list'))
        questions = response.context['object_list']

        self.assertEqual(questions.count(), 2)
        self.assertNotIn(self.question3, questions)

    def test_view_returning_message_when_no_questions(self):
        Question.objects.all().update(enabled=False)
        response = self.client.get(reverse('question_list'))

        self.assertContains(response, 'Não há pesquisas disponíveis.')
        
