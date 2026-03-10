from flask import Blueprint, jsonify, request
from app.models import Movie
from app import db

movies_bp = Blueprint('movies', __name__)


@movies_bp.route('/')
def list_movies():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)

    query = Movie.query.order_by(Movie.created_at.desc())
    pagination = query.paginate(page=page, per_page=per_page)

    return jsonify({
        'movies': [m.to_dict() for m in pagination.items],
        'total': pagination.total,
        'page': page,
        'pages': pagination.pages,
    })


@movies_bp.route('/<int:movie_id>')
def get_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return jsonify(movie.to_dict())


@movies_bp.route('/', methods=['POST'])
def create_movie():
    data = request.get_json()
    movie = Movie(
        title=data['title'],
        description=data.get('description'),
        release_year=data.get('release_year'),
        rating=data.get('rating'),
        image_url=data.get('image_url'),
        director=data.get('director'),
        genres=data.get('genres', []),
    )
    db.session.add(movie)
    db.session.commit()
    return jsonify(movie.to_dict()), 201


@movies_bp.route('/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    data = request.get_json()

    for field in ['title', 'description', 'release_year', 'rating', 'image_url', 'director', 'genres']:
        if field in data:
            setattr(movie, field, data[field])

    db.session.commit()
    return jsonify(movie.to_dict())


@movies_bp.route('/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return '', 204
