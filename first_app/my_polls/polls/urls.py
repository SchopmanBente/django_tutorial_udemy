from django.urls import path
from . import views
from .views import QuestionsListView

app_name = 'polls'

urlpatterns = [
    path('', QuestionsListView.as_view(), name="index"),
    path('<int:question_id>', views.detail, name="detail"),
    path('<int:question_id>/vote', views.vote, name="vote"),
    path('<int:question_id>/results', views.results, name="results")
]
