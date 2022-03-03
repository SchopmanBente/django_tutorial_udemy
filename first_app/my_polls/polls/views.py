# from django.template import loader,RequestContext

# from django.template import loader,RequestContext

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View

from .models import Question, Choice


# Create your views here.


class QuestionsListView(ListView):
    model = Question
    context_object_name = "Available polls"


def detail(request, question_id):
    try:
        q = Question.objects.get(pk=question_id)
        return render(request, "polls/detail-1.html", {"question": q})
    except Question.DoesNotExist:
        raise Http404("No Question matches the given query.")



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results-1.html', {'question': question,})

""" 
class ResultsView(View):
    model = Question
    template_name = 'polls/results-1.html'
"""

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["polls"])
    except:
        return render(request, "polls/detail-1.html",
                      {'question': question, 'error_message': "Please select a choice!"})

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args={question.id}))
        # return '{}<int:question_id>/results'.format(reverse('polls:results', kwargs={'question': question.pk,}))
