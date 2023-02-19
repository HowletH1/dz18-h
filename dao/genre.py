from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session
        self.model = Genre

    def get_one(self, gid):
        return self.session.query(self.model).get(gid)

    def get_all(self):
        return self.session.query(self.model).all()

    def create(self, data):
        ent = self.model(**data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d):
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()
