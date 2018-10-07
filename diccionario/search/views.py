from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from .models import Word, Meaning, Example, Origin
from django.template import loader
from django.utils import timezone
from .forms import NewWord
from random import sample


# Create your views here.


def index(request):
    latest_word_list = Word.objects.order_by('-pub_date')[:5]
    context = {'latest_word_list': latest_word_list}
    return render(request, 'search/index.html', context)


def detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    count = Word.objects.all().count()
    rand_ids = sample(range(1, count), 4)
    random_words = Word.objects.filter(id__in=rand_ids)

    return render(request, 'search/detail.html', {'word': word, 'random_words': random_words})


def aprobar(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = ApproveWords(request.POST)
            if form.is_valid():
                for wid in request.POST['approved_list']:
                    word = Word.objects.get(pk=wid)
                    word.approved = True
                    word.save()

                for wid in request.POST['delete_list']:
                    word = Word.objects.get(pk=wid)
                    word.delete()
        else:
            form = ApproveWords()
        return render(request, 'search/aprobar.html', {'form': form})
    else:
        redirect('/search')




def new_word(request):
    latest_word_list = Word.objects.order_by('-pub_date')[:5]
    context = {'latest_word_list': latest_word_list}

    if request.method == "POST":
        form = NewWord(request.POST)
        if form.is_valid():
            word_text = request.POST['word']
            word = Word.objects.filter(word_text=word_text)
            if word:
                redirect('/search/' + word[0].id)

            meaning = Meaning(meaning_text=request.POST['meaning'])
            meaning.save()

            if request.POST['example']:
                example = Example(example_text=request.POST['example'])
                example.save()
            if request.POST['origin']:
                origin = Origin(origin_text=request.POST['origin'])
                origin.save()

            word = Word(word_text=request.POST['word'], pub_date=timezone.now(), word_meaning=meaning, word_examples=example, word_origin=origin)
            word.save()
    else:
        form = NewWord()
    return render(request, 'search/new_word.html', {'form': form}, context)
