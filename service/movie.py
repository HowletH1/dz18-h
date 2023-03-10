from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_id(mid)

    def create(self, data):
        return self.dao.create(data)

    def delete(self, mid):
        self.dao.delete(mid)

    def update(self, data):
        self.dao.update(data)
        return self.dao
