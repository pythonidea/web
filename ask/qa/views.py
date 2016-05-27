# -*-coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage


def test(request, *args, **kwargs):
    return HttpResponse('OK')
#...должна работать пагинация.    
def paginate(request, questions):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
# Список "новых" вопросов.
def new_questions(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    return render(request, 'list.html', { 'page': page, 'title': 'new questions' })
# Список "популярных" вопросов.
def popular_questions(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    return render(request, 'list.html', { 'page': page, 'title': 'popular questions' })
# Страница одного вопроса
def one_question(request, id):
    question = get_object_or_404(Question, pk=id)
    questions = question.answer_set.all()
    page = paginate(request, questions)
    form = AnswerForm(initial={'question': question.pk })
    return render(request, 'question.html', { 'question': question, 'page': page, 'form': form })

