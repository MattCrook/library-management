import sqlite3
from django.shortcuts import render
from libraryapp.models import Library
from ..connection import Connection


def list_libraries(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_curser = conn.cursor()

        db_curser.execute("""
            SELECT
                l.id,
                l.title,
                l.address
            FROM libraryapp_library l
        """)

        all_libraries = []
        dataset = db_curser.fetchall()

        for row in dataset:
            library = Library()
            library.id = row['id']
            library.title = row['title']
            library.address = row['address']

        all_libraries.append(library)

    template = 'libraries/list.html'
    context = {
        'all_libraries': all_libraries
    }

    return render(request, template, context)
