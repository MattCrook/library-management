import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Librarian
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from libraryapp.models import model_factory


@login_required
def list_librarians(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            # conn.row_factory = sqlite3.Row

            conn.row_factory = model_factory(Librarian)
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT
                l.id,
                l.location_id,
                l.user_id,
                u.first_name,
                u.last_name,
                u.email
            FROM libraryapp_librarian l
            JOIN auth_user u on l.user_id = u.id
            """)
            all_librarians = db_cursor.fetchall()

        # all_librarians = []
        # dataset = db_cursor.fetchall()

        # for row in dataset:
        #     lib = Librarian()
        #     lib.id = row["id"]
        #     lib.location_id = row["location_id"]
        #     lib.user_id = row["user_id"]
        #     lib.first_name = row["first_name"]
        #     lib.last_name = row["last_name"]
        #     lib.email = row["email"]

        #     all_librarians.append(lib)

        template_name = 'librarians/list.html'
        context = {
            'all_librarians': all_librarians
        }
        return render(request, template_name, context)

    # elif request.method == 'POST':
    #     form_data = request.POST
    #     with sqlite3.connect(Connection.db_path) as conn:
    #         db_cursor = conn.cursor()
    #         db_cursor.execute("""
    #         INSERT INTO libraryapp_librarian
    #         (
    #             location_id, user_id
    #         )
    #         VALUES (?, ?)
    #         """,
    #         (form_data['location_id'], request.user.librarian.id))

    #     return redirect(reverse('libraryapp:books'))
