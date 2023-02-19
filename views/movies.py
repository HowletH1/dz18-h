from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all()
        res = MovieSchema(many=True).dump(movies)
        return res, 200

    def post(self):
        data = request.json
        movie = movie_service.create(data)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        movie_d = MovieSchema().dump(movie)
        return movie_d, 200

    def put(self, mid):
        data = request.json
        if "id" not in data:
            data["id"] = mid
        movie_service.update(data)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204
