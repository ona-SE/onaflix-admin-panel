#!/usr/bin/env bash
set -euo pipefail

# Start PostgreSQL, create user and database matching the app's connection string.
sudo service postgresql start

sudo -u postgres psql -c "CREATE USER gitpod WITH PASSWORD 'gitpod' CREATEDB;" 2>/dev/null || true
sudo -u postgres psql -c "CREATE DATABASE onaflix_admin OWNER gitpod;" 2>/dev/null || true
