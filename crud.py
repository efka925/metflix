from sqlalchemy.orm import sessionmaker
from models import eng, Movies, Series, User, Watchlist

Session = sessionmaker(bind=eng)
session = Session()

# CREATE


def create_movie(title, rating, release_year):
    session.add(Movies(title=title, rating=rating, release_year=release_year))
    session.commit()


def create_series(title, rating, release_year, amount_of_seasons):
    session.add(Series(title=title, rating=rating,
                release_year=release_year, amount_of_seasons=amount_of_seasons))
    session.commit()


def create_user(name, surname):
    session.add(User(name=name, surname=surname))
    session.commit()


def create_watching_list(name, date_when_created):
    session.add(Watchlist(name=name, date_when_created=date_when_created))
    session.commit()

# READ
def get_movies():
    return session.query(Movies).all()


def get_series():
    return session.query(Series).all()


def get_users():
    return session.query(User).all()


def get_watching_list():
    return session.query(Watchlist).all()



# UPDATE


def update_movie(id, title, rating, release_year):
    movie = session.query(Movies).filter_by(id=id).first()
    movie.title = title
    movie.rating = rating
    movie.release_year = release_year
    session.commit()


def update_series(id, title, rating, release_year, amount_of_seasons):
    series = session.query(Series).filter_by(id=id).first()
    series.title = title
    series.rating = rating
    series.release_year = release_year
    series.amount_of_seasons = amount_of_seasons
    session.commit()


def update_user(id, name, surname):
    user = session.query(User).filter_by(id=id).first()
    user.name = name
    user.surname = surname
    session.commit()


def update_watching_list(id, name, date_when_created):
    wlist = session.query(Watchlist).filter_by(id=id).first()
    wlist.name = name
    wlist.date_when_created = date_when_created
    session.commit()

# DELETE


def delete_movie(id):
    session.query(Movies).filter_by(id=id).delete()
    session.commit()


def delete_series(id):
    session.query(Series).filter_by(id=id).delete()
    session.commit()


def delete_user(id):
    session.query(User).filter_by(id=id).delete()
    session.commit()


def delete_wlist(id):
    session.query(Watchlist).filter_by(id=id).delete()
    session.commit()

def delete_all_data_from_tables():
    session.query(Movies).delete()
    session.query(Series).delete()
    session.query(User).delete()
    session.query(Watchlist).delete()
    session.commit()


if __name__ == "__main__":
    create_movie("The Godfather", 9, "1972")
    create_series("Breaking Bad", 9, "2008", 5)
    create_user("John", "Doe")
    create_watching_list("To watch", "2021-01-01")
    print(get_movies())
    print(get_series())
    print(get_users())
    print(get_watching_list())

    update_movie(1, "Simpsons Movie", 10, "2007")
    update_series(1, "Futurama", 10, "2008",6)
    update_user(1, "Mia", "Thermopolis")
    update_watching_list(1, "To watch later", "2021-01-01")

    delete_movie(1)
    delete_series(1)
    delete_user(1)
    delete_wlist(1)
    delete_all_data_from_tables()