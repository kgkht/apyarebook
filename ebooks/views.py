from django.shortcuts import render, get_object_or_404
from .models import Ebook, Category, Series
# Create your views here.


all_category = Category.objects.all()
all_series = Series.objects.all()
    

def home(request):
    ebooks = Ebook.objects.all()
    return render(request, 'ebooks/home.html',
                  {'ebooks': ebooks, 'category': all_category, 'series':all_series})


def ebook_category(request):

    return render(request, 'ebooks/category.html',
                  {'series': all_series, 'categories': all_category})


def single_category(request, category_id):
    category_info = get_object_or_404(Category, pk=category_id)
    category_part = Ebook.objects.filter(category=category_id)
    context = {'category_info': category_info, 'category_part': category_part, 'categories': all_category}
    return render(request, 'ebooks/singlecategory.html', context)



def ebook_series(request):

     return render(request, 'ebooks/series.html',
                   {'series': all_series, 'categories': all_category})



def ebook_detail(request, book_id):
    
    read_book = get_object_or_404(Ebook, pk=book_id)

    return render(request, 'ebooks/bookpost.html',
                  {'book': read_book, 'series': all_series})



def single_serie(request, serie_id):
    serie_info = get_object_or_404(Series, pk=serie_id)
    serie_part = Ebook.objects.filter(series=serie_id)
    context = {'serie_info': serie_info, 'serie_part': serie_part, 'series': all_series}
    return render(request, 'ebooks/singleserie.html', context)



def ebook_home(request):
    pass

