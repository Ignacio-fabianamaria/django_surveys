# https://docs.djangoproject.com/en/5.1/topics/testing/overview/

from django.test import TestCase
from ..models import Question, Option, Vote
from datetime import date


class BaseTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(text="Qual sua cor favorita?")
        self.option1 = Option.objects.create(text="verde", question=self.question)
        self.option2 = Option.objects.create(text="vermelho", question=self.question)


class QuestionTestCase(BaseTestCase):
    def test_question_creation(self):
        self.assertEqual(self.question.text, "Qual sua cor favorita?")
        self.assertEqual(self.question.created_at.date(), date.today())
        self.assertTrue(self.question.enabled)
        self.assertEqual(str(self.question), "Qual sua cor favorita?")


class OptionTestCase(BaseTestCase):
    def test_option_creation(self):

        self.assertEqual(self.option1.text, "verde")
        self.assertEqual(self.option2.text, "vermelho")
        self.assertEqual(self.option1.question, self.question)
        self.assertEqual(self.option2.question, self.question)
        self.assertEqual(self.question.option_set.count(), 2)
        self.assertEqual(str(self.option1), "verde")


class VoteTestCase(BaseTestCase):
    def test_vote_creation(self):
        vote = Vote.objects.create(option=self.option1)

        self.assertEqual(vote.option, self.option1)
        self.assertEqual(Vote.objects.count(), 1)
        self.assertEqual(vote.created_at.date(), date.today())
