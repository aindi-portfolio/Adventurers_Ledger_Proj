# Adventurers Ledger - GitHub Copilot Instructions

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Project Overview
Adventurers Ledger is a Django + React full-stack web application for managing D&D-style characters. The backend uses Django REST Framework with PostgreSQL, and the frontend uses React 18 with Vite build tool.

## CRITICAL: Known Issues and Workarounds

### INCOMPLETE REQUIREMENTS.TXT
The requirements.txt file is MISSING critical dependencies. You MUST install these additional packages:
```bash
pip install django-environ django-cors-headers aiohttp
```

### Network Restrictions
Some environments have network restrictions that prevent downloading certain packages:
- Cypress cannot be installed (use `npm install --ignore-scripts`)
- PyPI timeouts may occur (use longer timeouts: `pip install --timeout 300`)

### Database Setup Requirements
PostgreSQL requires manual user and permission configuration:
```bash
sudo service postgresql start
sudo -u postgres createuser [username]
sudo -u postgres createdb adventurers_db
sudo -u postgres psql -c "ALTER USER [username] CREATEDB;"
sudo -u postgres psql adventurers_db -c "GRANT ALL PRIVILEGES ON DATABASE adventurers_db TO [username];"
sudo -u postgres psql adventurers_db -c "GRANT ALL ON SCHEMA public TO [username];"
```

## Working Effectively

### Bootstrap and Build (COMPLETE SETUP - NEVER CANCEL)
Execute these commands in order. NEVER CANCEL long-running operations:

#### Backend Setup (5-10 minutes total)
```bash
cd Adventurers_Ledger_Proj/Back_End
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies - takes 2-3 minutes, NEVER CANCEL, timeout: 300 seconds
pip install --timeout 300 -r ../../requirements.txt
pip install --timeout 300 django-environ django-cors-headers aiohttp

# Create .env file (REQUIRED)
cat > .env << EOF
DJANGO_SECRET_KEY=your-development-secret-key-here
MY_RAWG_KEY=your-rawg-api-key-here
DB_NAME=adventurers_db
DB_USER=your-username
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
EOF

# Setup database (manual steps required)
sudo service postgresql start
sudo -u postgres createuser your-username
sudo -u postgres createdb adventurers_db
sudo -u postgres psql -c "ALTER USER your-username CREATEDB;"
sudo -u postgres psql adventurers_db -c "GRANT ALL PRIVILEGES ON DATABASE adventurers_db TO your-username;"
sudo -u postgres psql adventurers_db -c "GRANT ALL ON SCHEMA public TO your-username;"

# Run migrations - takes 30-60 seconds, NEVER CANCEL, timeout: 300 seconds
python manage.py migrate

# Verify setup
python manage.py check
```

#### Frontend Setup (1-2 minutes total)
```bash
cd ../Front_End

# Install dependencies - takes 30 seconds, NEVER CANCEL, timeout: 180 seconds
# Note: Use --ignore-scripts if Cypress fails due to network restrictions
npm install --ignore-scripts

# Verify setup
npm run build  # Takes 1-2 seconds
```

### Running the Application

#### Start Backend Server
```bash
cd Adventurers_Ledger_Proj/Back_End
source venv/bin/activate
python manage.py runserver
# Runs on http://127.0.0.1:8000
```

#### Start Frontend Development Server
```bash
cd Adventurers_Ledger_Proj/Front_End
npm run dev
# Runs on http://localhost:5173
```

### Build and Test Commands

#### Backend Commands
```bash
# Development server
python manage.py runserver

# Database operations - NEVER CANCEL, timeout: 300 seconds
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Django shell
python manage.py shell

# Run system checks
python manage.py check
```

#### Frontend Commands
```bash
# Development server (instant startup)
npm run dev

# Production build - takes 1-2 seconds, NEVER CANCEL, timeout: 120 seconds
npm run build

# Preview production build
npm run preview

# Cypress tests (may fail due to network restrictions)
npm run cy:open        # Interactive mode - may not work
npm run cy:run         # Headless mode - may not work
```

## Validation and Testing

### ALWAYS run these validation steps after making changes:

#### Backend Validation
1. `python manage.py check` - System check
2. `python manage.py migrate --check` - Migration check
3. Start server and verify http://127.0.0.1:8000 responds

#### Frontend Validation
1. `npm run build` - Production build test
2. Start dev server and verify http://localhost:5173 responds
3. Check console for errors

#### Full Stack Testing
1. Start both backend (port 8000) and frontend (port 5173) servers
2. Verify frontend can communicate with backend APIs
3. Test user registration/login flow if authentication is required

## Troubleshooting

### Missing Dependencies Error
If you see "ModuleNotFoundError" for django-environ, corsheaders, or aiohttp:
```bash
pip install django-environ django-cors-headers aiohttp
```

### Database Connection Issues
1. Ensure PostgreSQL is running: `sudo service postgresql start`
2. Verify user exists and has permissions (see database setup above)
3. Check .env file has correct database credentials

### Cypress Installation Fails
Use: `npm install --ignore-scripts` to skip Cypress installation

### Network Timeout Issues
Use longer timeouts: `pip install --timeout 300` or `npm install --timeout 300000`

### CORS Issues
The django-cors-headers package must be installed and enabled in settings.py

## File Locations and Navigation

### Key Backend Files
- **Settings**: `Back_End/Adventurers_Ledger_Proj/settings.py`
- **Main URLs**: `Back_End/Adventurers_Ledger_Proj/urls.py`
- **Models**: Each app has models.py (character_app, item_app, etc.)
- **Environment**: `Back_End/.env` (must be created manually)

### Key Frontend Files
- **Main App**: `Front_End/src/App.jsx`
- **Entry Point**: `Front_End/src/main.jsx`
- **Vite Config**: `Front_End/vite.config.js`
- **Styles**: `Front_End/src/styles/` and Tailwind CSS

### Django Apps Structure
- **character_app**: Character management and inventory
- **item_app**: Items and equipment system  
- **monster_app**: Monster encounters
- **quest_app**: Quest management
- **shop_app**: Shopping system
- **user_app**: User authentication

## Common Development Tasks

### Adding New Features
1. Backend: Create/modify models, views, serializers, URLs
2. Frontend: Create/modify components in `src/components/` or `src/pages/`
3. Always test both build processes after changes

### Database Changes
1. `python manage.py makemigrations`
2. `python manage.py migrate` 
3. Test with `python manage.py check`

### API Development
- Backend APIs are in each app's views.py
- Frontend API calls are in `src/services/`
- Authentication uses Django REST Framework tokens

## External Dependencies

### APIs Used
- **D&D 5e API**: https://www.dnd5eapi.co (free, no auth required)
- **RAWG API**: https://api.rawg.io (requires API key in MY_RAWG_KEY env var)

### Required Environment Variables
```bash
DJANGO_SECRET_KEY=your-secret-key
MY_RAWG_KEY=your-rawg-api-key  
DB_NAME=adventurers_db
DB_USER=your-username
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

## Performance Notes

### Build Times (typical)
- Backend dependency installation: 2-3 minutes
- Frontend dependency installation: 30 seconds  
- Database migrations: 30-60 seconds
- Frontend build: 1-2 seconds
- Frontend dev server startup: ~500ms

### NEVER CANCEL Commands
Always use appropriate timeouts and wait for completion:
- `pip install` operations: 300+ seconds timeout
- `npm install` operations: 180+ seconds timeout  
- Database migrations: 300+ seconds timeout
- Any build processes: 120+ seconds timeout

## Network Considerations

Some environments have restricted network access:
- Use `--ignore-scripts` for npm install if Cypress fails
- Use `--timeout 300` for pip install if PyPI timeouts occur
- Some package downloads may fail - document alternatives in instructions