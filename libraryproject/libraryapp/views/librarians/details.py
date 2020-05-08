import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, Librarian
from libraryapp.models import model_factory
from ..connection import Connection

def create_librarian(cursor, row):
    _row = sqlite3.Row(cursor, row)

    librarian = Librarian()
    librarian.id = _row["librarian_id"]
    librarian.first_name = _row["first_name"]
    librarian.last_name = _row["last_name"]
    librarian.location = _row["location_id"]
    librarian.username = _row["username"]

    library = Library()
    library.id = _row["library_id"]
    library.title = _row["library_name"]
    library.address = _row["library_address"]

    librarian.library = library

    return librarian

def get_librarian(librarian_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_librarian
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                l.id librarian_id,
                l.location_id,
                l.user_id,
                u.first_name,
                u.last_name,
                u.username,
                loc.id library_id,
                loc.title library_name,
                loc.address library_address
            FROM libraryapp_librarian l
            JOIN libraryapp_library loc ON l.id = loc.id
            JOIN auth_user u ON u.id = l.user_id
            WHERE l.id = ?
        """ , (librarian_id,))
        return db_cursor.fetchone()

@login_required
def librarian_details(request, librarian_id):
    if request.method == 'GET':
        librarian = get_librarian(librarian_id)
        template_name = 'librarians/detail.html'
        return render(request, template_name, {'librarian': librarian})

    elif request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()
                db_cursor.execute("""
                DELETE FROM libraryapp_librarian
                WHERE id = ?
                """ , (librarian_id))
            return redirect(reverse('libraryapp:librarians'))
