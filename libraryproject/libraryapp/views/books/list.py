import sqlite3
from django.shortcuts import render
from libraryapp.models import Book
from ..connection import Connection
from libraryapp.models import model_factory
from django.shortcuts import redirect
from django.urls import reverse


# LOGIN_REDIRECT_URL set in settings.py file. Login_required is django decorator in which we specified the redirect url in settings.py
from django.contrib.auth.decorators import login_required


# This function is now called a view since it will handle HTTP requests, which we define in urlspy

@login_required
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            conn.row_factory = model_factory(Book)

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            all_books = db_cursor.fetchall()

            # all_books = []
            # dataset = db_cursor.fetchall()

            # for row in dataset:
            #     book = Book()
            #     book.id = row['id']
            #     book.title = row['title']
            #     book.isbn = row['isbn']
            #     book.author = row['author']
            #     book.year_published = row['year_published']
            #     book.librarian_id = row['librarian_id']
            #     book.location_id = row['location_id']

            #     all_books.append(book)

        # When a view wants to generate some HTML representations of data, it needs to specify a template to use.
        # template variable is holding the path and filename of the template in templates/books/list.html
        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        # Render method takes the HTTP request as the first argument, the template to be used as the second argument, and then a dictionary containing the data to be used in the template.
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_book
            (
                title, author, isbn,
                year_published, location_id, librarian_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['author'],
                form_data['isbn'], form_data['year_published'],
                request.user.librarian.id, form_data["location"]))

        return redirect(reverse('libraryapp:books'))
