<div align="center">

  <img src="static/images/icon.svg" alt="Taska Logo" width="80" height="80"/>

  <h1>Taska</h1>
  <p><strong>Smart Task Management System</strong></p>

  <!-- Badges -->
  ![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?style=for-the-badge&logo=flask&logoColor=white)
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
  ![Pandas](https://img.shields.io/badge/Pandas-3.0.2-150458?style=for-the-badge&logo=pandas&logoColor=white)
  ![NumPy](https://img.shields.io/badge/NumPy-2.4.4-013243?style=for-the-badge&logo=numpy&logoColor=white)
  ![WebSockets](https://img.shields.io/badge/WebSockets-SocketIO-010101?style=for-the-badge&logo=socketdotio&logoColor=white)
  ![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

  <br/>

  [![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-taska--2noj.onrender.com-1D9E75?style=for-the-badge)](https://taska-2noj.onrender.com)

</div>

---

## 📌 About

Taska is a full-stack smart task management web application built with **Flask + PostgreSQL**. It supports user authentication, full CRUD task management, real-time WebSocket notifications, and a Pandas/NumPy-powered analytics dashboard with CSV export.


---

## 🎥 Demo
![demo.gif](static/images/demo.gif)



---

## ✨ Features

- 🔐 **Authentication** — Register, Login, Logout with bcrypt password hashing
- ✅ **Task CRUD** — Create, Read, Update, Delete tasks with priority & status
- 📊 **Analytics Dashboard** — Pandas + NumPy powered stats with Chart.js doughnut chart
- 📥 **CSV Export** — Download your task report as a `.csv` file
- ⚡ **Real-time Updates** — WebSocket (Flask-SocketIO) live task list sync
- 🛡️ **Security** — User-scoped tasks, bcrypt hashing, login-required routes
- 📱 **Responsive UI** — Works on mobile and desktop

---

## 🖼️ Snapshot

![Login](static/images/login.png) 
![Dashboard](static/images/dashboard.png)
![Analytics](static/images/analytics.png)
![Supabase](static/images/supabase.png)|
---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask, Flask-SocketIO |
| Database | PostgreSQL (Supabase) |
| ORM | SQLAlchemy + Flask-Migrate |
| Auth | Flask-Login + Flask-Bcrypt |
| Analytics | Pandas, NumPy |
| Frontend | HTML, CSS, JavaScript, Chart.js |
| Real-time | WebSockets (Flask-SocketIO + gevent) |
| Deployment | Render (app) + Supabase (DB) |


## 📁 Project Structure

```
Taska/
├── app/
│   ├── __init__.py          # App factory (create_app)
│   ├── models.py            # SQLAlchemy models (User, Task)
│   ├── auth/
│   │   └── routes.py        # /register, /login, /logout
│   ├── tasks/
│   │   └── routes.py        # CRUD API endpoints
│   ├── analytics/
│   │   ├── routes.py        # /analytics, /analytics/export
│   │   └── service.py       # Pandas/NumPy logic
│   └── sockets/
│       └── events.py        # WebSocket event handlers
├── templates/               # Jinja2 HTML templates
├── static/                  # CSS, JS, images
├── migrations/              # Flask-Migrate auto-generated
├── schema.sql               # Database schema export
├── config.py                # App configuration
├── run.py                   # Entry point
├── requirements.txt         # Pinned dependencies
├── .env.example             # Environment variable template
└── README.md
```

---

---

## 🗄️ Database Schema

```sql
-- Users table
CREATE TABLE users (
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    email         VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tasks table
CREATE TABLE tasks (
    id          SERIAL PRIMARY KEY,
    title       VARCHAR(200) NOT NULL,
    description TEXT,
    priority    VARCHAR(20) NOT NULL DEFAULT 'medium',  -- low | medium | high
    status      VARCHAR(20) NOT NULL DEFAULT 'pending', -- pending | in_progress | completed
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
);
```

---

## 📡 API Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/auth/register` | Register new user | ❌ |
| POST | `/auth/login` | Login user | ❌ |
| GET | `/auth/logout` | Logout user | ✅ |
| GET | `/api/tasks` | Get all tasks | ✅ |
| POST | `/api/tasks` | Create task | ✅ |
| PUT | `/api/tasks/<id>` | Update task | ✅ |
| DELETE | `/api/tasks/<id>` | Delete task | ✅ |
| GET | `/api/analytics` | Get analytics stats | ✅ |
| GET | `/api/analytics/export` | Download CSV report | ✅ |

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.10+
- PostgreSQL installed and running
- Git

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/Manglam11/Taska.git
cd Taska
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory (see `.env.example`):
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://postgres:password@localhost:5432/taska_db
```

**5. Create the database**
```bash
# In psql
CREATE DATABASE taska_db;
```

**6. Run migrations**
```bash
flask db upgrade
```

**7. Start the server**
```bash
python run.py
```

Visit `http://127.0.0.1:5000` 🎉

---

## 🌐 Deployment

- **App hosted on:** [Render](https://render.com)
- **Database hosted on:** [Supabase](https://supabase.com)
- **Live URL:** [https://taska-2noj.onrender.com](https://taska-2noj.onrender.com)

> ⚠️ Free tier on Render spins down after inactivity. First load may take 30–50 seconds.

---



## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Flask session secret key |
| `DATABASE_URL` | PostgreSQL connection string |

See `.env.example` for the template.

---

## 👨‍💻 Author

**Manglam**

[![GitHub](https://img.shields.io/badge/GitHub-Manglam11-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Manglam11)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Manglam-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/manglam-dubey/)

---

<div align="center">
  <i>"First, solve the problem. Then, write the code."</i>
</div>