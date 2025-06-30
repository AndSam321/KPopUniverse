# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kpop Universe is a full-stack social platform for K-pop fans, built with Django REST Framework (backend) and Angular (frontend). The project follows a clear separation between backend API and frontend client application.

## Architecture

### Backend (Django)
- **Location**: `/backend/`
- **Framework**: Django 5.2.3 with Django REST Framework
- **Database**: SQLite (development), PostgreSQL (production)
- **Apps**: 
  - `users/` - User authentication and profiles
  - `posts/` - Content creation and management
  - `rooms/` - Community groups/fandoms
  - `notifications/` - Real-time notifications
- **Key Dependencies**: django-cors-headers, pillow, psycopg2-binary, python-decouple

### Frontend (Angular)
- **Location**: `/frontend/kpop-universe-frontend/`
- **Framework**: Angular 19.2.0
- **Testing**: Jasmine + Karma
- **Build System**: Angular CLI

## Common Commands

### Backend (Django)
```bash
cd backend

# Development server
python manage.py runserver

# Database operations
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Testing
python manage.py test

# Create new app
python manage.py startapp app_name

# Environment setup
python -m venv venv
source venv/bin/activate  # Mac/Linux
# or venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Frontend (Angular)
```bash
cd frontend/kpop-universe-frontend

# Development server
ng serve
# or
npm start

# Build
ng build
ng build --configuration production

# Testing
ng test

# Generate components/services
ng generate component component-name
ng generate service service-name

# Install dependencies
npm install
```

## Development Workflow

1. **Backend Development**: 
   - Activate virtual environment first
   - Create/update models, then run migrations
   - Use Django admin for data management
   - API endpoints follow `/api/[app-name]/` pattern

2. **Frontend Development**:
   - Angular project uses standalone components (modern Angular approach)
   - Component files follow Angular naming conventions
   - Uses TypeScript with strict type checking

3. **Environment Configuration**:
   - Backend uses `.env` files with python-decouple
   - Database currently SQLite for development
   - CORS configured for frontend-backend communication

## Branch and Commit Conventions

- **Branches**: `feature/backend-[name]`, `feature/frontend-[name]`, `fix/[description]`
- **Commits**: `backend: [description]`, `frontend: [description]`, `docs: [description]`

## Key Files to Know

- `backend/kpop_universe_backend/settings.py` - Django configuration
- `backend/requirements.txt` - Python dependencies
- `frontend/kpop-universe-frontend/package.json` - Node.js dependencies and scripts
- `frontend/kpop-universe-frontend/angular.json` - Angular CLI configuration

## Development Notes

- Project uses modern Angular (v19) with standalone components
- Backend has CORS configured for frontend communication
- SQLite used for development simplicity, PostgreSQL for production
- No linting configuration found - consider adding ESLint (frontend) and flake8/black (backend)