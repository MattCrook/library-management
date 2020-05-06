import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import model_factory
from ..connection import Connection
from libraryapp.views.books.form import get_libraries
from libraryapp.models import Librarian


def get_librarians():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Librarian)
        db_cursor = conn.cursor()
        db_cursor.execute("""
                SELECT
                    l.id,
                    l.location_id,
                    b.user_id,
                    library.title,
                    library.address,
                    u.first_name,
                    u.last_name,
                    u.email
                FROM libraryapp_librarian l
                JOIN libraryapp_library ON library.address = l.location_id
                JOIN auth_user u on l.user_id = u.id
                """)
        return db_cursor.fetchone()


@login_required
def librarian_form(request):
    if request.method == 'GET':
        librarians = get_librarians()
        template = 'librarian/form.html'
        context = {
            'all_librarians': librarians
        }
        return render(request, template, context)
