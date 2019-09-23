from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(requset, question_id):
    question  = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(requset, 'polls/detail.html', context)


def results(request, question_id):
    result = "You're looking at the results of question %s."
    return HttpResponse(result % question_id)


def vote(requset, question_id):
    result = "You're voting the question %s."
    return HttpResponse(result % question_id)