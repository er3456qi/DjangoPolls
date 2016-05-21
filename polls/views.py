from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

# use generic view replaced
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    """
     The template_name attribute is used to tell Django.
     to use a specific template name instead of the auto generated default template name.
     because by default, generic.ListView use a template called '<app name>/<model name>_list.html'
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    """
        For DetailView the question variable is provided automatically – since we’re using a Django model (Question),
        Django is able to determine an appropriate name for the context variable.
        However, for ListView, the automatically generated context variable is question_list.
        To override this we provide the context_object_name attribute,
        specifying that we want to use latest_question_list instead.
    """
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You did not select a choice.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data. This
        # This prevents data from being posted twice if a user hits the Back button.
        # reverse() helps avoid having to hardcode a URL in the view function.
        # It is given the name of the view that we want to pass control to and
        # the variable portion of the URL pattern that points to that view.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))



