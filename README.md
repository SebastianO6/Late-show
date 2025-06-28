# Late Show API

A RESTful API for managing late night TV show episodes, guests, and appearances.

## Features

 JWT Authentication
 CRUD operations for episodes, guests, and appearances
 PostgreSQL database
 Flask REST API

## Setup

### Prerequisites
 Python 
 PostgreSQL
 pipenv

### Installation

1. Clone the repository:
   git clone https://github.com/yourusername/late-show-api.git
   cd late-show-api

2. Install dependencies:
   pipenv install
   pipenv shell

3. Set up database:
   createdb late_show_db


4. Run migrations:
   flask db upgrade

5. Seed the database:
   python server/seed.py

## Running the Server
python server/app.py

## API Endpoints

### Authentication
 `POST /register` - Register new user
 `POST /login` - Login and get JWT token

### Episodes
 `GET /episodes` - List all episodes
 `GET /episodes/<id>` - Get episode details
 `DELETE /episodes/<id>` - Delete episode 

### Guests
 `GET /guests` - List all guests

### Appearances
 `POST /appearances` - Create new appearance 

