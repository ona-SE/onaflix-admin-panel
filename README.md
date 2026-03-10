# OnaFlix Admin Panel

Internal admin dashboard for managing the OnaFlix movie catalog. Built with Flask and PostgreSQL.

## Stack

- **Language:** Python 3.11+
- **Framework:** Flask 3.0
- **ORM:** Flask-SQLAlchemy
- **Database:** PostgreSQL
- **Auth:** Flask-Login
- **Server:** Gunicorn

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

## API Endpoints

- `GET /` -- Service info
- `GET /health` -- Health check
- `GET /stats` -- Dashboard statistics
- `GET /movies` -- List movies (paginated)
- `GET /movies/:id` -- Get movie
- `POST /movies` -- Create movie
- `PUT /movies/:id` -- Update movie
- `DELETE /movies/:id` -- Delete movie
- `POST /auth/login` -- Admin login
- `POST /auth/logout` -- Admin logout

## Testing

```bash
pytest
```
