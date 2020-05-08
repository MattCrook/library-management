from django.urls import path
from .views import *
from django.urls import include, path



# This file will define all of the URLs that your library application
# will respond to.
#These (two) patterns ensures that HTTP requests to
# Are handled by the book_list() function in the views/books/list.py module.



app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),

    path('books/', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),

    path('libraries/', library_list, name='libraries'),
    path('library/form', library_form, name='library_form'),
    path('libraries/<int:library_id>/form/', library_edit_form, name='library_edit_form'),
    path('libraries/<int:library_id>/details/', library_details, name='library'),

    path('librarians/', list_librarians, name='librarians'),
    path('librarian/form', librarian_form, name='librarian_form'),
    path('librarians/<int:librarian_id>/details/', librarian_details, name='librarian'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),

]
