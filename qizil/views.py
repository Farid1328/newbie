from django.shortcuts import render, redirect
from . models import Gold, Comment
from . forms import Goldform, Commentform
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


def index(request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')

    gold = Gold.objects.filter(Q(name__icontains=search) |
                               Q(gram__icontains=search)
                               )
    result = 5
    page = request.GET.get('pager')
    pagi = Paginator(gold, result)
    try:
        gold = pagi.page(page)
    except PageNotAnInteger:
        page = 1
        gold = pagi.page(page)
    except EmptyPage:
        page = pagi.num_pages
        gold = pagi.page(page)
    context ={'gold': gold, 'pagi' : pagi, 'search' : search}
    return render(request, 'qizil/index.html', context)


def gold(request, pk):
    goldid = Gold.objects.get(id=pk)
    form = Commentform()
    if request.method == 'POST':
        form = Commentform(request.POST)
        comment = form.save(commit=False)
        comment.comment = goldid
        comment.owner = request.user
        comment.save()
    context = {'goldid': goldid, 'form': form}
    return render(request, 'qizil/gold_info.html', context)


def addgold(request):
    page = 'new'
    form = Goldform()
    if request.method == 'POST':
        form = Goldform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, 'page': page}
    return render(request, 'qizil/goldform.html', context)


def editgold(request, pk):
    gold = Gold.objects.get(id=pk)
    form = Goldform(instance=gold)
    if request.method == 'POST':
        form = Goldform(request.POST,request.FILES ,instance=gold, )
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'qizil/goldform.html', context)


def delgold(request, pk):
    page = 'delete'
    gold = Gold.objects.get(id=pk)
    form = Goldform()
    if request.method == 'POST':
        form = Goldform(instance=gold)
        gold.delete()
        return  redirect('index')
    context = {'gold': gold, 'page': page}
    return render(request, 'qizil/goldform.html', context)
