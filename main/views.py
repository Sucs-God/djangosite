from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, Http404
import os
from djangoProject1 import settings

from .models import Books, Sections


# Create your views here.
class SectionsViewIndex(View):
    '''Тест вывод секций'''

    def get(self, request):
        sections = Sections.objects.all()
        return render(request, 'main/use/test.html', {'sections_list': sections})

class SectionsViewCatalog(View):
    '''Тест вывод секций'''

    def get(self, request):
        sections = Sections.objects.all()
        return render(request, 'main/use/catalog.html', {'sections_list': sections})


class BooksView(View):
    '''Список книг'''

    def get(self, request, section):
        section1 = Sections.objects.get(url=section)
        books = Books.objects.filter(sections__url=section)
        data = {'book_list': books,
                'section_item': section1
                }
        return render(request, 'main/use/books_list.html', data)


class BookDetailView(View):
    '''Полное описание фильма'''

    def get(self, request, section, slug):
        book = Books.objects.get(url=slug)
        return render(request, 'main/use/some_book.html', {'book': book})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/file_book')
            response['Content-Disposition'] = f'inline;filename ={os.path.basename(file_path)}'
            return response
    raise Http404


def about(request):
    return render(request, 'main/use/about_site.html')


def catalog(request):
    return render(request, 'main/use/catalog.html')

#
# def beginner(request):
#     return render(request, 'main/for_beginner.html')
#
#
# def pro(request):
#     return render(request, 'main/for_pro.html')
#
#
# def directories(request):
#     return render(request, 'main/directory.html')
