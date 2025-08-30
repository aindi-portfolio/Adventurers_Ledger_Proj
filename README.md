# Adventurers Ledger

A full-stack web application for managing D&D-style adventuring characters, including character creation, inventory management, monster encounters, quests, and shopping experiences.

## 🎯 Project Overview

Adventurers Ledger is a comprehensive character management system inspired by Dungeons & Dragons. Players can create and customize characters, manage inventories, engage in combat encounters with monsters, complete quests, and visit shops to buy and sell items. The application features a fantasy-themed UI with custom styling and integrates with third-party APIs for rich game content.

## 🛠️ Technology Stack

### Backend
- **Django 4.2.23** - Web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Primary database
- **Token Authentication** - User authentication system
- **python-dotenv** - Environment variable management
- **psycopg** - PostgreSQL adapter
- **requests** - HTTP library for API calls

### Frontend
- **React 18** - User interface library
- **Vite** - Build tool and development server
- **TailwindCSS 4.1** - Utility-first CSS framework with custom fantasy theme
- **Axios** - HTTP client for API communication
- **React Router DOM** - Client-side routing
- **Bootstrap 5.3** - Additional UI components

### Development & Testing
- **Cypress** - End-to-end testing framework
- **ESLint** - Code linting and formatting

## 🌐 Third-Party APIs

### D&D 5e API
- **URL**: `https://www.dnd5eapi.co`
- **Purpose**: Fetching D&D equipment, monsters, and game content
- **Usage**: Seeding items and monsters for the game database
- **Authentication**: None required (free API)

### RAWG API
- **URL**: `https://api.rawg.io`
- **Purpose**: Gaming data and content
- **Usage**: Additional gaming content and data caching
- **Authentication**: API key required
- **Environment Variable**: `MY_RAWG_KEY`

## 📋 Prerequisites

### System Requirements
- **Node.js** 18+ and npm
- **Python** 3.8+
- **PostgreSQL** 12+
- **Git**

### Required Accounts
- RAWG API account for gaming data (get free API key at [rawg.io](https://rawg.io/apidocs))

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/aindi-portfolio/Adventurers_Ledger_Proj.git
cd Adventurers_Ledger_Proj
```

### 2. Backend Setup (Django)

#### Navigate to Backend Directory
```bash
cd Adventurers_Ledger_Proj/Back_End
```

#### Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Install Python Dependencies
```bash
pip install -r ../requirements.txt
```

#### Environment Variables Setup
Create a `.env` file in the `Back_End` directory:
```bash
# Backend/.env
DJANGO_SECRET_KEY=your-secret-key-here
MY_RAWG_KEY=your-rawg-api-key-here
DB_NAME=adventurers_db
DB_USER=your-postgres-username
DB_PASSWORD=your-postgres-password
DB_HOST=localhost
DB_PORT=5432
```

#### Database Setup
```bash
# Create PostgreSQL database
createdb adventurers_db

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 3. Frontend Setup (React)

#### Navigate to Frontend Directory
```bash
cd ../Front_End
```

#### Install Node Dependencies
```bash
npm install
```

## 🏃‍♂️ Running the Application

### Start Backend Server
```bash
cd Adventurers_Ledger_Proj/Back_End
source venv/bin/activate  # On Windows: venv\Scripts\activate
python manage.py runserver
```
The Django API will be available at `http://localhost:8000`

### Start Frontend Development Server
```bash
cd Adventurers_Ledger_Proj/Front_End
npm run dev
```
The React application will be available at `http://localhost:5173`

### Seeding Data
Once both servers are running and you've created a user account:
1. Log into the application
2. Use the seeding functions to populate the database with:
   - Items from D&D 5e API
   - Monsters from D&D 5e API
   - Initial game content

## 📁 Project Structure

```
Adventurers_Ledger_Proj/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── package.json                       # Root package configuration
│
├── Adventurers_Ledger_Proj/
│   ├── Back_End/                      # Django backend
│   │   ├── Adventurers_Ledger_Proj/   # Main Django project
│   │   │   ├── settings.py            # Django configuration
│   │   │   └── urls.py                # Main URL routing
│   │   ├── character_app/             # Character management
│   │   ├── item_app/                  # Item and inventory system
│   │   ├── monster_app/               # Monster encounters
│   │   ├── quest_app/                 # Quest management
│   │   ├── shop_app/                  # Shopping system
│   │   ├── user_app/                  # User authentication
│   │   ├── api_playground.py          # RAWG API integration
│   │   ├── manage.py                  # Django management script
│   │   └── .env                       # Environment variables
│   │
│   └── Front_End/                     # React frontend
│       ├── src/
│       │   ├── components/            # Reusable UI components
│       │   ├── pages/                 # Page components
│       │   ├── services/              # API service functions
│       │   ├── context/               # React context providers
│       │   ├── styles/                # Custom CSS
│       │   ├── App.jsx                # Main app component
│       │   └── main.jsx               # Entry point
│       ├── public/                    # Static assets
│       ├── package.json               # Frontend dependencies
│       ├── vite.config.js             # Vite configuration
│       └── tailwind.config.js         # TailwindCSS configuration
```

## 🛠️ Development Commands

### Backend Commands
```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run Django shell
python manage.py shell
```

### Frontend Commands
```bash
# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run Cypress tests
npm run cy:open        # Interactive mode
npm run cy:run         # Headless mode
```

## 🎮 Key Features

- **Character Creation & Management**: Create and customize D&D-style characters
- **Inventory System**: Manage equipment, weapons, and items
- **Combat Encounters**: Battle monsters with turn-based combat
- **Quest System**: Complete quests and earn rewards
- **Shopping**: Buy and sell items at various shops
- **Progressive Character Development**: Level up and improve stats
- **Fantasy-Themed UI**: Custom TailwindCSS styling with medieval/fantasy aesthetic

## 🔐 Authentication

The application uses Django REST Framework's token-based authentication:
- User registration and login through dedicated endpoints
- Secure token storage in browser localStorage
- Protected routes requiring authentication
- User profile management

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Issues**
   - Ensure PostgreSQL is running
   - Verify database credentials in `.env` file
   - Check if database `adventurers_db` exists

2. **API Key Issues**
   - Verify `MY_RAWG_KEY` is set in `.env` file
   - Check RAWG API key validity at [rawg.io](https://rawg.io)

3. **Frontend Not Loading**
   - Ensure Node.js 18+ is installed
   - Run `npm install` in the Frontend directory
   - Check if backend server is running on port 8000

4. **CORS Issues**
   - Backend includes CORS middleware for frontend communication
   - Verify frontend is running on port 5173

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure functionality
5. Submit a pull request

## 📝 License

This project is for educational and portfolio purposes. Please respect the terms of service for third-party APIs used.

---

**Happy Adventuring!** 🗡️⚔️🛡️