from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse

from .models import Choice, Question

# Create your views here.

def index(request):
    return render(request, "polls/index.html", {
        "questions": Question.objects.order_by("-pub_date")[:5]
    })


def detail(request, question_id):
    try:
        context = {
            "question": Question.objects.get(pk=question_id)
        }
    except Question.DoesNotExist:
        raise Http404(f"No question found with id ${question_id}")
    return render(request, "polls/detail.html", context)
    

def results(request, question_id):
    try:
        context = {
            "question": Question.objects.get(pk=question_id)
        }
    except Question.DoesNotExist:
        raise Http404(f"No question found with id ${question_id}")
    return render(request, "polls/results.html", context)



def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f"No question found with id ${question_id}")
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Please select a choice"
        })
    
    selected_choice.votes = F("votes") + 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
