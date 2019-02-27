from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from .models import Word, Meaning, Example, Origin
from django.template import loader
from django.utils import timezone
from .forms import NewWord, ApproveWord
from random import sample
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    # latest_word_list = Word.objects.order_by('-pub_date')[:6]
    latest_word_list = Word.objects.filter(approved=True).order_by('-pub_date')[:6]
    context = {'latest_word_list': latest_word_list}
    return render(request, 'search/index.html', context)


def detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    count = Word.objects.all().count()
    rand_ids = sample(range(1, count+1), 4 if count >= 4 else count)
    if  word.id in rand_ids:
        rand_ids.remove(word.id)
    random_words = Word.objects.filter(id__in=rand_ids)

    return render(request, 'search/detail.html', {'word': word, 'random_words': random_words})


def aprobar(request):
    if request.user.is_superuser:
        words = Word.objects.filter(approved=False)
        if request.method == "POST":
            form = ApproveWord(request.POST)
            if form.is_valid():
                wid = request.POST['word_id']
                word = Word.objects.get(pk=wid)
                if request.POST['button'] == 'aprobar':
                    word.approved = True
                    word.save()
                elif request.POST['button'] == 'eliminar':
                    word.delete()
        else:
            form = ApproveWord()
            
        context = {'words' : words, 'form': form}
        return render(request, 'search/aprobar.html', context)
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

            if request.POST['example']:
                example = Example(example_text=request.POST['example'])
                example.save()
            if request.POST['origin']:
                origin = Origin(origin_text=request.POST['origin'])
                origin.save()

            word = Word(word_text=request.POST['word'], pub_date=timezone.now(), word_examples=example, word_origin=origin)
            word.save()

            all_meanings = request.POST['meaning']
            meanings = []
            for m in all_meanings:
                meaning = Meaning(meaning_text=m, word=word)
                meaning.save()
    else:
        form = NewWord()
    return render(request, 'search/new_word.html', {'form': form}, context)


def search(request):
  if request.GET:
    searcher = request.GET["searcher"]
    number = len(Word.objects.all())
    words = Word.objects.filter(word_text__contains=searcher, approved=True)
    # Caso donde no haya palabras que coincidan con la busqueda
    if len(words) == 0:
        context = {'busqueda' : searcher}
        return render(request, 'search/no_results.html', context)
    page = request.GET.get('page', 1)
    paginator = Paginator(words, len(words))
    try:
      catalogo = paginator.page(page)
    except PageNotAnInteger:
      catalogo = paginator.page(1)
    except EmptyPage:
      catalogo = paginator.page(paginator.num_pages)
    pagscount = paginator.count
    number = len(Word.objects.all())
    context = {'busqueda' : words, 'pagscount' : pagscount, 'number' : number}
  return render(request, "search/results.html", context)

def search_letter(request):
  if request.GET:
    searcher = request.GET["searcher"]
    searcher = searcher.lower()
    number = len(Word.objects.all())
    words = Word.objects.filter(word_text__contains=searcher)
    wordlist = []
    for word in words:
        if str(word).startswith(searcher):
            wordlist.append(word)
    # Caso donde no haya palabras con esa letra
    if len(wordlist) == 0:
        return render(request, 'search/no_results.html')
    page = request.GET.get('page', 1)
    paginator = Paginator(wordlist, len(wordlist))
    try:
      catalogo = paginator.page(page)
    except PageNotAnInteger:
      catalogo = paginator.page(1)
    except EmptyPage:
      catalogo = paginator.page(paginator.num_pages)
    pagscount = paginator.count
    number = len(Word.objects.all())
    context = {'busqueda' : wordlist, 'pagscount' : pagscount, 'number' : number}
  return render(request, "search/results.html", context)
