# Task Manager Backend

This repository contains the backend for the Task Manager application, built using Flask and SQLite.

Check out the wiki for project updates [wiki](https://github.com/RoyH11/Note-Task-Manager/wiki).

## Project Structure
```
.
├── LICENSE
├── README.md
└── backend
    ├── app.py
    ├── models.py
    ├── routes.py
    ├── migrations/
    ├── instance/
    │   └── tasks.db
```

## Getting Started
### Prerequisites
Ensure you have the following installed:
- Python 3.9+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-CORS
- Flask-JWT-Extended
- Conda (for environment management)

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd backend
   ```
2. Create a Conda environment:
   ```sh
   conda create --name task-manager python=3.9
   conda activate task-manager
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   Create a `.env` file in the `backend` directory and add:
   ```
   JWT_SECRET_KEY=your_secret_key
   ```

### Database Setup & Migration
We use Flask-Migrate for handling database migrations.

1. Initialize the migration directory (only needed once):
   ```sh
   flask db init
   ```
2. Generate a new migration (whenever models change):
   ```sh
   flask db migrate -m "Initial migration"
   ```
3. Apply the migration (creates/modifies the database schema):
   ```sh
   flask db upgrade
   ```

### Running the Application
To start the Flask server:
```sh
python app.py
```
By default, the application runs on `http://127.0.0.1:5000/`.

### API Endpoints
- `GET /` - Check if the API is running.
- Additional routes for tasks and users will be added later.

### Notes
- The `instance/` directory contains the SQLite database and should be ignored in version control.
- The `migrations/` folder tracks database schema changes and should be committed.

Let me know if you need further clarification! 🚀

