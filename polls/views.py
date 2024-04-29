from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.views import generic

from .forms import getVoteForm
from .models import Choice, Question


def from_htmx(request) -> bool:
    """"Checks if request is from HTMX"""
    return bool(request.headers.get('HX-Request'))

def get_template(name, hx=False) -> str:
    """Returns polls/base_{name}.html for templates if request is not from HTMX"""
    return f"polls/{name if hx else f"base_{name}"}.html"

    
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


def get_vote_form_view(request, question_id, context={}):
    question = get_object_or_404(Question, pk=question_id)
    hx = from_htmx(request)
    template = get_template('detail', hx=hx)
    
    _context = {
        "form": getVoteForm(question)(),
        "question": question,
        "loading": not hx,
    }
    _context.update(context)
    
    return render(request, template, _context)


def detail(request, question_id):
    return get_vote_form_view(request, question_id)


def results(request, question_id):
    return get_vote_form_view(request, question_id, {"submitted": True})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
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
