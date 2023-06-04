from flask import render_template, request, redirect
from app import app
from models.book_list import books, add_new_book, remove_book_by_index
from models.book import Book



@app.route("/")
def book_list():
    return render_template('index.html', book_list=books)

@app.route("/", methods=['POST'])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    description = request.form["description"]
    available = False if "available" in request.form else True
    book = Book(title, author, genre, description, available)
    add_new_book(book)
    return redirect("/")


@app.route("/del/<index>", methods=["POST"])
def remove_book(index):
    remove_book_by_index(int(index))
    return redirect("/")


@app.route("/book/<index>", methods=["POST"])
def book_info(index):
    book_info = books[int(index)]
    return render_template('book.html', book=book_info, book_list=books)


@app.route("/check_out/<index>", methods=["POST"])
def check_out(index):
    book = books[int(index)]
    book.available = False
    return redirect("/")


@app.route("/check_in/<index>", methods=["POST"])
def check_in(index):
    book = books[int(index)]
    book.available = True
    return redirect("/")

