# Local Development Setup

This document explains how to set up the Adventurers Ledger application for local development.

## Prerequisites

- Python 3.8+
- Node.js 18+
- PostgreSQL 12+

## Backend Setup

### 1. Navigate to the Backend Directory
```bash
cd Adventurers_Ledger_Proj/Back_End
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r ../../requirements.txt
```

### 4. Environment Variables Setup
Create a `.env` file based on the `.env.example` file:
```bash
cp .env.example .env
```

Then edit the `.env` file with your actual values:
```
# Django Configuration
DJANGO_SECRET_KEY=your-secret-key-for-local-development

# Database Configuration  
DB_NAME=adventurers_db
DB_USER=your-postgresql-username
DB_PASSWORD=your-postgresql-password
DB_HOST=localhost
DB_PORT=5432

# Third-party API Keys
MY_RAWG_KEY=your-rawg-api-key-here
OPENROUTER_API_KEY=your-openrouter-api-key-here
```

### 5. Database Setup
```bash
# Create PostgreSQL database
createdb adventurers_db

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 6. Start Backend Server
```bash
python manage.py runserver
```
The Django API will be available at `http://localhost:8000`

## Frontend Setup

### 1. Navigate to Frontend Directory
```bash
cd Adventurers_Ledger_Proj/Front_End
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Start Frontend Development Server
```bash
npm run dev
```
The React application will be available at `http://localhost:5173`

## API Keys Information

### RAWG API Key
- Used for game data in the API playground
- Get your free key at: https://rawg.io/apidocs
- Optional for basic functionality

### OpenRouter API Key  
- Used for AI-powered quest generation
- Get your key at: https://openrouter.ai/
- Optional for basic functionality

## Troubleshooting

1. **Database Connection Issues**: Ensure PostgreSQL is running and the database exists
2. **Environment Variables**: Make sure the `.env` file is in the `Back_End` directory
3. **Port Conflicts**: Backend uses port 8000, frontend uses port 5173
4. **CORS Issues**: The backend includes CORS middleware for frontend communication

## Verification

After setup, you should be able to:
- Access the Django admin at `http://localhost:8000/admin`
- Access the React app at `http://localhost:5173`
- See API documentation at `http://localhost:8000/api/`