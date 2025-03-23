# Note-Task-Manager

This is a full-stack task/note manager web application built with **Flask** for the backend and **React (Vite)** for the frontend. It supports creating, viewing, updating, and deleting tasks tied to specific users.

Check out the wiki for project updates [wiki](https://github.com/RoyH11/Note-Task-Manager/wiki).


---

## 📁 Project Structure
```
.
├── LICENSE
├── README.md
├── backend
│   ├── __pycache__/
│   ├── app.py
│   ├── instance/
│   ├── migrations/
│   ├── models.py
│   ├── routes.py
│   └── seed_db.py
├── frontend
│   ├── README.md
│   ├── eslint.config.js
│   ├── index.html
│   ├── node_modules/
│   ├── package-lock.json
│   ├── package.json
│   ├── public/
│   ├── src/
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
├── package.json
└── requirements.txt
```

---

## 🔧 Backend Setup (Flask)
1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create and activate Conda environment** (or use your preferred Python environment)
   ```bash
   conda create -n task-manager-dev python=3.9
   conda activate task-manager-dev
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   flask db upgrade
   ```

5. **(Optional) Seed mock data**
   ```bash
   python seed_db.py
   ```

6. **Start the Flask server**
   ```bash
   python app.py
   ```
   API will be available at `http://localhost:5000`

---

## ⚛️ Frontend Setup (React + Vite)
1. **Navigate to the project root**
   ```bash
   cd ~/Projects/Note-Task-Manager
   ```

2. **Ensure Volta is installed**
   If not:
   ```bash
   curl https://get.volta.sh | bash
   exec $SHELL
   volta install node
   volta install npm
   volta pin node
   volta pin npm
   ```

3. **Create React app (if not already created)**
   ```bash
   npm create vite@latest frontend -- --template react
   cd frontend
   npm install
   ```

4. **Start the frontend dev server**
   ```bash
   npm run dev
   ```
   React app will be available at `http://localhost:5173`

---


## 💅 Tailwind CSS (Frontend Styling)
refer to [Tailwind Docs](https://tailwindcss.com/docs/installation/using-vite) for installation and setup.

---

## 🧠 API Endpoints (Backend)
- `GET /users` - list all users
- `POST /users` - create a user
- `GET /tasks` - list all tasks
- `POST /tasks` - create a task
- `PUT /tasks/<id>` - update a task
- `DELETE /tasks/<id>` - delete a task

---

Let me know if you need any help catching up or want to build a feature! ✨
