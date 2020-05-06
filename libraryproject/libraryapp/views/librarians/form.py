# import sqlite3
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from libraryapp.models import model_factory
# from ..connection import Connection
# from libraryapp.views.books.form import get_libraries
# from libraryapp.models import Librarian

# def get_librarians():
#         with sqlite3.connect(Connection.db_path) as conn:
#             conn.row_factory = model_factory(Librarian)
#             db_cursor = conn.cursor()
#             db_cursor.execute("""
#                 SELECT
#                 b.id,
#                 b.title,
#                 b.isbn,
#                 b.author,
#                 b.year_published,
#                 b.librarian_id,
#                 b.location_id
#             FROM libraryapp_book b
#             WHERE b.id = ?
#             """, (book_id,))
#             return db_cursor.fetchone()




# @login_required
# def librarian_form(request):
#     if request.method == 'GET':
#         librarians = get_librarian()
#         template = 'librarian/form.html'
#         context = {
#             'all_librarians': librarians
#         }
#         return render(request, template, context)
