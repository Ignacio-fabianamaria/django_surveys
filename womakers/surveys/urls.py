from django.urls import path
from .views import QuestionListView, QuestionDetailView, VoteCreateView


urlpatterns = [
    path("", QuestionListView.as_view(), name='question_list'),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
    path("<int:pk>/vote", VoteCreateView.as_view(), name="question_vote"),
]
