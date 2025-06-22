# 🎵 Kpop Universe

A vibrant community platform for K-pop fans worldwide! Kpop Universe combines the best of social platforms like Reddit with a sleek, modern UX tailored specifically for fandom culture.

## 🌟 Features

- **User Authentication & Profiles** - Personalized fan profiles with favorite artists and groups
- **Post Creation** - Share text, images, links, and media content
- **Rooms** - Join community groups for specific fandoms, artists, or K-pop events
- **Interactive Discussions** - Comment and engage in threaded conversations
- **Content Moderation** - Community-driven moderation tools
- **Real-time Notifications** - Stay updated on post activity and room updates
- **Mobile-Friendly** - Optimized for both desktop and mobile experiences

## 🏗️ Tech Stack

### Backend
- **Django** - Python web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Primary database
- **AWS S3** - Media storage (planned)

### Frontend
- **Angular** - TypeScript-based frontend framework
- **Angular Material** - UI component library
- **Tailwind CSS** - Utility-first CSS framework
- **SCSS** - Enhanced CSS with variables and mixins

### Infrastructure
- **AWS** - Cloud deployment and services
- **Docker** - Containerization (planned)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL 12+
- Git

### Backend Setup (Django)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd kpop-universe
   ```

2. **Set up Python environment**
   ```bash
   cd backend
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials and secret key
   ```

5. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://localhost:8000/`

### Frontend Setup (Angular)

1. **Navigate to frontend directory**
   ```bash
   cd frontend/kpop-universe-frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the development server**
   ```bash
   ng serve
   ```

   The application will be available at `http://localhost:4200/`

## 📁 Project Structure

```
kpop-universe/
├── backend/                 # Django REST API
│   ├── kpop_universe_backend/
│   ├── accounts/           # User authentication
│   ├── posts/              # Post management
│   ├── rooms/              # Community rooms
│   ├── notifications/      # Notification system
│   ├── requirements.txt
│   └── manage.py
├── frontend/               # Angular application
│   └── kpop-universe-frontend/
│       ├── src/
│       ├── angular.json
│       └── package.json
├── .gitignore
├── README.md
└── CONTRIBUTING.md
```

## 🛠️ Development

### API Endpoints
- **Authentication**: `/api/auth/`
- **Posts**: `/api/posts/`
- **Rooms**: `/api/rooms/`
- **Users**: `/api/users/`
- **Notifications**: `/api/notifications/`

### Key Commands

**Backend:**
```bash
# Create new Django app
python manage.py startapp app_name

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test
```

**Frontend:**
```bash
# Generate new component
ng generate component component-name

# Generate new service
ng generate service service-name

# Build for production
ng build --prod

# Run tests
ng test
```

## 🎨 Design Principles

- **Fan-First**: Every feature designed with K-pop fans in mind
- **Performance**: Fast loading times for media-heavy content
- **Mobile Responsive**: Seamless experience across all devices
- **Engaging UI**: Vibrant, modern design that feels alive
- **Community Focused**: Tools that foster discussion and connection

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Branch Naming Convention
- `feature/backend-[feature-name]` - Backend features
- `feature/frontend-[feature-name]` - Frontend features
- `fix/[issue-description]` - Bug fixes
- `docs/[update-description]` - Documentation updates

### Commit Message Format
- `backend: [description]` - Backend changes
- `frontend: [description]` - Frontend changes
- `docs: [description]` - Documentation
- `config: [description]` - Configuration files

## 📋 Roadmap

- [ ] User authentication system
- [ ] Basic post creation and viewing
- [ ] Room creation and management
- [ ] Comment system
- [ ] Notification system
- [ ] Real-time chat features
- [ ] Media upload and optimization
- [ ] Content moderation tools
- [ ] Mobile app (future)

## 🔧 Environment Variables

Create a `.env` file in the backend directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=kpop_universe_db
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

## 📱 Screenshots

*Coming soon - screenshots will be added as features are developed*

## 🐛 Known Issues

- None currently - project is in initial development phase

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](../../issues) section
2. Create a new issue with detailed information
3. Contact the development team

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the vibrant K-pop community
- Built with love for fans, by fans
- Special thanks to all contributors

---

**Made with 💜 for the K-pop community**
