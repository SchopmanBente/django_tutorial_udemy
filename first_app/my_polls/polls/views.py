from django.http import HttpResponse
#from django.template import loader,RequestContext
from django.http import Http404

from django.shortcuts import render, get_object_or_404

from .models import Question
from django.views.generic import ListView

# Create your views here.

class QuestionsListView(ListView):
    model = Question
    context_object_name = "Available polls"

def detail(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)
        return render(request, "polls/detail.html", {"question": q})
    except Question.DoesNotExist:
        raise Http404("No Question matches the given query.")



def results(request, question_id):
    return HttpResponse("These are the results of the question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)
