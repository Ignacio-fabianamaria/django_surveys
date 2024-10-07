# https://docs.djangoproject.com/en/5.1/topics/testing/overview/

from django.test import TestCase
from .models import Question
from datetime import date


class QuestionTestCase(TestCase):

    def test_question_creation(self):
        question = Question.objects.create(text="Qual sua cor favorita?")

        self.assertEqual(question.text, "Qual sua cor favorita?")
        self.assertEqual(question.created_at.date(), date.today())
        self.assertTrue(question.enabled)

    def test_question_string(self):
        question = Question.objects.create(text="Qual sua cor favorita?")

        self.assertEqual(str(question), "Qual sua cor favorita?")