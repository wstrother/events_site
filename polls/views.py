from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import F
# from django.urls import reverse
from django.views import generic

from .forms import getVoteForm

from .models import Choice, Question
    
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f"No question found with id ${question_id}")
    
    form = getVoteForm(question.choice_set.all())()
    
    return render(request, 'polls/base_detail.html', {
        "question": question,
        "form": form,
        "submitted": False
    })


def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f"No question found with id ${question_id}")
    
    form = getVoteForm(question.choice_set.all())()
    
    return render(request, 'polls/detail.html', {
        "question": question,
        "form": form,
        "submitted": True
    })


def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f"No question found with id ${question_id}")
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choices"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Please select a choice"
        })
    
    selected_choice.votes = F("votes") + 1
    selected_choice.save()
    return HttpResponseRedirect(f"/polls/results/{question_id}")


def test_htmx(request):
    return HttpResponse('Test response')