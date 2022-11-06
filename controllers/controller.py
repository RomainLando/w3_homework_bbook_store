from flask import render_template
from models import book_list
from app import app


@app.route('/')
def index():
    return render_template('index.html', title="Pandora's Books")

@app.route('/books')
def show_books():
    return render_template('books.html', books=book_list.books, title="Pandora's Books")

@app.route('/books/<index>')
def show_book(index):
    return render_template('book.html', book=book_list.books[int(index)], title="Pandora's Books", index=index)

@app.route('/books/delete/<index>', methods=['POST'])
def delete_book(index):
    book_list.books.pop(int(index))
    return render_template('books.html', books=book_list.books, title="Pandora's Books")

@app.route('/books/update/<index>', methods=['POST'])
def check_book(index):
    book = book_list.books[int(index)]
    book.checked_out = False if book.checked_out else True
    return render_template('books.html', books=book_list.books, title="Pandora's Books")