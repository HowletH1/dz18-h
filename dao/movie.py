from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_id(self, mid):
        return self.session.query(Movie).get(mid)

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        movie = self.get_id(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, data):
        movie = self.get_id(data.get("id"))
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")
        movie.title = data.get("title")
        movie.rating = data.get("rating")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")

        self.session.add(movie)
        self.session.commit()
