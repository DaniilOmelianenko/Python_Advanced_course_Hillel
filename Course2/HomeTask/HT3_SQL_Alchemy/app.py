from flask import Flask, render_template, request, redirect
from forms import AuthorForm, BookForm, GenreForm, session
from models import Author, Genre, Book


app = Flask(__name__)


def create_form_handler(form_class, model_class, title):
    form = form_class()
    success = False
    if request.method == "POST":
        form = form_class(request.form)
        if form.validate():
            temp_object = model_class()
            form.populate_obj(temp_object)  # добавляем обхект автора
            session.add(temp_object)
            session.commit()
            success = True
    return render_template(
        'add_object.html', **{
            'form': form,
            'title': title,
            'success': success
        }
    )


@app.route('/add_book/', methods=['GET', 'POST'])
def add_book():
    return create_form_handler(BookForm, Book, 'Add Book')


@app.route('/add_author/', methods=['GET', 'POST'])
def add_author():
    return create_form_handler(AuthorForm, Author, 'Add Author')


@app.route('/add_genre/', methods=['GET', 'POST'])
def add_genre():
    return create_form_handler(GenreForm, Genre, 'Add Genre')


@app.route('/<int:book_id>/update', methods=['GET', 'POST'])
def book_update(book_id):
    book = session.query(Book).filter(Book.id == book_id).one()
    form = BookForm(obj=book)
    success = False
    if request.method == 'POST':
        form = BookForm(request.form)
        if form.validate():
            form.populate_obj(book)
            session.add(book)
            session.commit()
            success = True
    return render_template(
        'book_update.html', **{
            'book_id': book,
            'form': form,
            'success': success})


@app.route('/')
def home():
    books = session.query(Book)
    genre = dict(session.query(Genre.name, Genre.id))
    year = [year.year for year in books]
    query = request.args
    for key, value in query.items():
        if value != "ALL":
            if value in genre.keys():
                value = genre.get(value)
            books = books.filter_by(**{key: value})
    return render_template(
        'index.html', **{'books': books, 'genre': genre, 'year': year}
    )


@app.route('/<int:book_id>')
def book_detail(book_id):
    book = session.query(Book).get(book_id)
    return render_template(
        'book_detail.html', **{
            'book': book
        }
    )


@app.route('/<int:book_id>/del')
def book_delete(book_id):
    book = session.query(Book).get(book_id)
    try:
        session.delete(book)
        session.commit()
        return redirect('/')
    except:
        return "При удалении книги произошла ошибка"


if __name__ == '__main__':
    app.run(debug=True)
