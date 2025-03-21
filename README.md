# Note-Task-Manager

This is a full-stack task/note manager web application built with **Flask** for the backend and **React (Vite)** for the frontend. It supports creating, viewing, updating, and deleting tasks tied to specific users.

Check out the wiki for project updates [wiki](https://github.com/RoyH11/Note-Task-Manager/wiki).


---

## 📁 Project Structure
```
Note-Task-Manager/
├── backend/        # Flask API
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── seed_db.py
│   └── migrations/
├── frontend/       # React app (Vite)
│   ├── src/
│   ├── public/
│   └── .env
└── README.md
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

## 🌐 Connecting Frontend to Backend
In `frontend/.env`:
```env
VITE_API_BASE=http://localhost:5000
```
Use it in code like this:
```js
fetch(`${import.meta.env.VITE_API_BASE}/tasks`)
```

---

## 💅 Tailwind CSS (Frontend Styling)
1. **Install Tailwind CSS**
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

2. **Configure `tailwind.config.js`**
   ```js
   content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"]
   ```

3. **Import Tailwind into `src/index.css`**
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

---

## 🧠 API Endpoints (Backend)
- `GET /users` - list all users
- `POST /users` - create a user
- `GET /tasks` - list all tasks
- `POST /tasks` - create a task
- `PUT /tasks/<id>` - update a task
- `DELETE /tasks/<id>` - delete a task

---

## 🚀 What's Next
- [ ] Add task editing & deletion in frontend
- [ ] Add user selector in create task form
- [ ] JWT-based authentication
- [ ] Save user sessions

Let me know if you need any help catching up or want to build a feature! ✨
