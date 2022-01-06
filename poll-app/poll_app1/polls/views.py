# tutorial part 4
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# tutorial part 5
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # tutorial 5
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




# tutorial part 3
""" 
from django import template
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, response, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView( generic.ListView ):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        "Return the last five published questions"
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    

class ResultsView( generic.DetailView ):
    model = Question
    template_name = 'polls/results.html'
    

    
# tutorial part 3
def index( request ):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    
    return render( request, 'polls/index.html', context )
    


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# Tutorial part 3
def results( request, question_id ):
    response = "You're looking at the results of qestion %s."
    
    return HttpResponse( response % question_id )
    
# Tutorial part 4
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote( request, question_id ):
    # tutorial part 3
    #return HttpResponse( "You're voting on question %s." % question_id )
    
    # tutorial part 4
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
    question = get_object_or_404( Question, pk=question_id )
    try:
        selected_choice = question.choice_set.get( pk=request.POST['choice'] )
        
    except (KeyError, Choice.DoesNotExist):
        return render( request, 'polls/detail.html', {
            'question': question,
            'error_message' : "You didn't select a choice"
        } )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect( reverse( 'polls:results', args=
                                             (question.id, )) )
"""