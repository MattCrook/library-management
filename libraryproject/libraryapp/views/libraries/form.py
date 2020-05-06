import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection
from libraryapp.views.books.form import get_libraries
from libraryapp.views.libraries.details import get_library


@login_required
def library_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'libraries/form.html'
        context = {
            'all_libraries': libraries
        }
        return render(request, template, context)

@login_required
def library_edit_form(request, library_id):
    if request.method == 'GET':
        library = get_library(library_id)
        libraries = get_libraries()
        template = 'libraries/form.html'
        context = {
            'library': library,
            'all_libraries': libraries
        }

        return render(request, template, context)
