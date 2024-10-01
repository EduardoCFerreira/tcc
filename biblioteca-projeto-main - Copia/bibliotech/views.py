from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from bibliotech.models import Book
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    livros = Book.objects.all().order_by('-id')
    return render(request, 'bibliotech/pages/home.html', context={
        'livros': livros,
    })

def category(request, category_id):
    livros = get_list_or_404(
        Book.objects.filter(
            category__id=category_id
        ).order_by('-id')
    )

    return render(request, 'bibliotech/pages/category.html', context={
        'livros': livros,
        'title': f'{livros[0].category.name}'
    })

def book(request, id):
    livro = get_object_or_404(Book, pk=id)

    return render(request, 'bibliotech/pages/livro-view.html', context={
        'livro': livro,
        'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404
    
    livros = Book.objects.filter(
        title__icontains=search_term
    ).order_by('-id')

    return render(request, 'bibliotech/pages/search.html', context={
        'page_title': f'Search for "{search_term}" |',
        'livros': livros,
    })
