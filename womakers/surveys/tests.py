# https://docs.djangoproject.com/en/5.1/topics/testing/overview/

from django.test import TestCase
from .models import Question, Option
from datetime import date


class BaseTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(text="Qual sua cor favorita?")


class QuestionTestCase(TestCase):
    def test_question_creation(self):
        self.assertEqual(self.question.text, "Qual sua cor favorita?")
        self.assertEqual(self.question.created_at.date(), date.today())
        self.assertTrue(self.question.enabled)

    def test_question_string(self):
        self.assertEqual(str(self.question), "Qual sua cor favorita?")


class OptionTestCase(TestCase):
    def test_option_creation(self):
        option1 = Option.objects.create(text="verde", question=self.question)
        option2 = Option.objects.create(text="vermelho", question=self.question)

        self.assertEqual(option1.text, "verde")
        self.assertEqual(option2.text, "vermelho")
        self.assertEqual(option1.question, self.question)
        self.assertEqual(option2.question, self.question)
        self.assertEqual(self.question.option_set.count(), 2)

    def test_question_string(self):
        option = Option.objects.create(text="verde", question=self.question)

        self.assertEqual(str(option), "verde")
