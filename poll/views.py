# views.py
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Question, Choice

def home(request):
    questions = Question.objects.all()
    return render(request, 'poll/home.html', {"questions": questions})

def vote(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    if request.method == "POST":
        try:
            choice_id = request.POST.get('choice')
            print(choice_id)
            choice = q.choice_set.get(pk=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('poll:result', q_id)
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'poll/vote.html', {
                "question": q,
                "error_message": "DEBES DE ELEGIR ALGO PARA VOTAR"
            })
    return render(request, 'poll/vote.html', {"question": q})

def result(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    choices = q.choice_set.all()
    choice_texts = [choice.choice_text for choice in choices]
    votes = [choice.votes for choice in choices]

    return render(request, 'poll/result.html', {
        "question": q,
        "choice_texts": choice_texts,
        "votes": votes,
    })

