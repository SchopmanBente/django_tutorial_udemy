from django.urls import path
from . import views
from .views import QuestionsListView

urlpatterns = [
    path('', QuestionsListView.as_view(), name="Index"),
    path('<int:question_id>', views.detail, name="Detail"),
    path('<int:question_id>/vote', views.vote, name="Vote"),
    path('<int:question_id>/results', views.results, name="Results")
]
