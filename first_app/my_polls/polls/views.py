# from django.template import loader,RequestContext

# from django.template import loader,RequestContext

from django.http import Http404 , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404 , reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, UpdateView, View

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


def results(request, polls, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choosen_choice = get_object_or_404(Choice, pk=polls)
    return render(request, 'polls/results-1.html', {'question': question, 'choosen_choice': choosen_choice, })


class ResultsView(View):
    model = Choice
    template_name = 'polls/results-1.html'


def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk= request.POST["choice"])
    except:
        return  render(request, "polls/detail-1.html", {'question': question, 'error_message':"Please select a choice!"})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls/results-1.html', args={question.id}) )


@method_decorator(csrf_protect, name='dispatch')
class VoteView(UpdateView):
    model = Choice
    fields = [
        "choice_text",
        "votes",
        "question",
    ]
    success_url = "<int:question_id>/results"
    template_name = "results-1.html"

    def post(self, request, **kwargs):
        # question_id = request.POST['question']
        # question = get_object_or_404(Question, pk=question_id)

        model = request.POST.get('question_id')
        choice_id = request.POST.get('choice')
        return HttpResponseRedirect(request, 'polls/results-1.html', {'question_id': model, 'choice_id': choice_id, })
