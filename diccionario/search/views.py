from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Word, Meaning, Example, Origin
from django.template import loader
from django.utils import timezone
from .forms import NewWord


# Create your views here.


def index(request):
    latest_word_list = Word.objects.order_by('-pub_date')[:5]
    context = {'latest_word_list': latest_word_list}
    return render(request, 'search/index.html', context)


def detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    return render(request, 'search/detail.html', {'word': word})


def new_word(request):
    latest_word_list = Word.objects.order_by('-pub_date')[:5]
    context = {'latest_word_list': latest_word_list}

    if request.method == "POST":
        form = NewWord(request.POST)
        if form.is_valid():
            meaning = Meaning(meaning_text=request.POST['meaning'])
            meaning.save()

            if request.POST['example']:
                example = Example(example_text=request.POST['example'])
                example.save()
            if request.POST['origin']:
                origin = Origin(origin_text=request.POST['origin'])
                origin.save()

            word = Word(word_text=request.POST['word'], pub_date=timezone.now(), word_meaning=meaning.id, word_example=example.id, word_origin=origin.id)
            word.save()
    else:
        form = NewWord()
        return render(request, 'search/new_word.html', {'form': form}, context)
