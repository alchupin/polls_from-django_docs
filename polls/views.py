from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '. '.join([q.question for q in latest_question_list])
    return HttpResponse(output)


def detail(requset, question_id):
    return HttpResponse("You're looking at question %s," % question_id)


def results(request, question_id):
    result = "You're looking at the results of question %s."
    return HttpResponse(result % question_id)


def vote(requset, question_id):
    result = "You're voting the question %s."
    return HttpResponse(result % question_id)