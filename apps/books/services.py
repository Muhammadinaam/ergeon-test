from django.db.models import Count

from .models import Author, Book


def print_books_with_authors_4_1():
    books = Book.objects.prefetch_related('author')

    for book in books:
        print(f'"{book.title}". {book.author.name}')


def print_author_with_all_books_4_2():
    authors = Author.objects.prefetch_related('book_set')

    for author in authors:
        books = ', '.join(
            [f'"{book.title}"' for book in author.book_set.all()]
        )
        print(f'{author.name}: {books}')


def print_authors_with_books_count_decending_order_4_3():
    data = Book.objects.prefetch_related('author').values(
        'author__name'
    ).annotate(count=Count('author__name')).order_by('-count')

    for item in data:
        print(f'{item["author__name"]}: {item["count"]}')
