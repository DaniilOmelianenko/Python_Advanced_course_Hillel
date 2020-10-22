from engine_db import engine
from sqlalchemy.orm import sessionmaker
from wtforms.ext.sqlalchemy.orm import model_form
from models import Book, Author, Genre


session = sessionmaker(bind=engine)()


BookForm = model_form(Book, db_session=session)
AuthorForm = model_form(Author, db_session=session)
GenreForm = model_form(Genre, db_session=session)
