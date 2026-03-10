from flask import Blueprint, jsonify

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
def index():
    return jsonify({
        'service': 'OnaFlix Admin Panel',
        'version': '1.0.0',
        'endpoints': ['/movies', '/auth', '/health'],
    })


@dashboard_bp.route('/stats')
def stats():
    from app.models import Movie, AdminUser
    from app import db

    movie_count = db.session.query(Movie).count()
    user_count = db.session.query(AdminUser).count()

    return jsonify({
        'movies': movie_count,
        'admin_users': user_count,
    })
