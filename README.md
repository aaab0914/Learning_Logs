# 📚 Learning Log

A Django-based web application for tracking your learning journey. Create topics, write journal entries, and build your personal knowledge base.

## ✨ Features

- **User Authentication** - Secure registration and login system
- **Topic Management** - Create and organize learning topics
- **Learning Entries** - Write detailed journal entries for each topic
- **Entry Editing** - Update and refine your learning notes
- **Personal Dashboard** - View all your topics and entries in one place
- **User Privacy** - Each user can only access their own content

## 🛠️ Tech Stack

- **Backend**: Django 3.x
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Authentication**: Django built-in user authentication

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aaab0914/learning-log.git
   cd learning-log
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to project directory**
   ```bash
   cd ll_project
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`

## 📖 Usage

### Getting Started

1. **Register** - Create a new account on the home page
2. **Login** - Sign in with your credentials
3. **Create Topic** - Add a new learning topic
4. **Add Entry** - Write a journal entry about what you learned
5. **Edit Entry** - Update your entries anytime
6. **View Progress** - See all your topics and entries

### Main Pages

- **Home** - Welcome page with login/register options
- **Topics** - View all your learning topics
- **Topic Detail** - See all entries for a specific topic
- **New Topic** - Create a new learning topic
- **New Entry** - Add an entry to a topic
- **Edit Entry** - Modify an existing entry

## 📁 Project Structure

```
learning-log/
├── ll_project/                 # Main Django project
│   ├── ll_project/            # Project settings
│   ├── learning_logs/         # Main app
│   │   ├── models.py          # Topic and Entry models
│   │   ├── views.py           # View functions
│   │   ├── forms.py           # Django forms
│   │   ├── urls.py            # URL routing
│   │   └── templates/         # HTML templates
│   ├── accounts/              # User authentication app
│   │   ├── views.py           # Registration/login views
│   │   └── templates/         # Auth templates
│   └── manage.py              # Django management script
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔐 Security Features

- User authentication required for all learning features
- Each user can only access their own topics and entries
- CSRF protection on all forms
- Secure password handling

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a learning project to demonstrate Django web development concepts.

## 🎓 Learning Outcomes

This project demonstrates:
- Django MVT (Model-View-Template) architecture
- User authentication and authorization
- Database relationships (Foreign Keys)
- Form handling and validation
- URL routing
- Template inheritance
- Django ORM

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Happy Learning!** 🌟
