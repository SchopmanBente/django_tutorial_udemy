from django.http import HttpResponse
#from django.template import loader,RequestContext
from .models import Question
from django.views.generic import ListView

# Create your views here.
"""
def index(request):
    latest_questions = Question.objects.order_by('-publish_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
     'latest_questions': latest_questions
    })
    servertemplate = loader.select_template(template).template

    return HttpResponse(servertemplate)
*/
"""
class QuestionsListView(ListView):
    model = Question
    context_object_name = "Available polls"
def detail(request, question_id):
    return HttpResponse("This is the detail view of question: %s" % question_id)


def results(request, question_id):
    return HttpResponse("These are the results of the question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)
