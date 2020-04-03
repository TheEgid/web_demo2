from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Answer, Question
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET


def page(request):
    object_list = Question.objects.all()
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    if not page:
        page = 1
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    all_pages = int(paginator.num_pages)
    return render(request, 'page.html',
                  {'page': page,
                   'all_pages': all_pages,
                   'questions': questions,
                   })


def popular_page(request):
    object_list = Question.objects.popular()
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')

    if not page:
        page = 1
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    all_pages = int(paginator.num_pages)
    return render(request, 'popular_page.html',
                  {'page': page,
                   'all_pages': all_pages,
                   'questions': questions,
                   })


@require_GET
def question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    return render(request, 'question.html', {
        'question': question,
    })


def test(request, *args, **kwargs):
    return HttpResponse('Ny_OK')


# def index(request):
#     return render(request, 'index.html')
#

#return render(request, 'catalog_main.html', context)