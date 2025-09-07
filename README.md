


# Reimagined Finance

A full-stack finance application with a React + Vite frontend and a Python (FastAPI) backend.

---

## Project Structure

```
Reimagined-Finance/
├── backend/      # Python FastAPI backend
│   ├── main.py
│   ├── db.py
│   ├── app.db
│   └── requirements.txt
└── frontend/     # React + Vite frontend
	 ├── src/
	 ├── public/
	 ├── package.json
	 └── ...
```

---

## Prerequisites

- Node.js (v18+ recommended)
- npm (comes with Node.js)
- Python 3.10+
- (Optional) Virtualenv for Python

---

## Backend Setup (FastAPI)

1. **Navigate to the backend folder:**
	```powershell
	cd backend
	```
2. **(Optional) Create and activate a virtual environment:**
	```powershell
	python -m venv venv
	.\venv\Scripts\activate
	```
3. **Install dependencies:**
	```powershell
	pip install -r requirements.txt
	```
4. **Run the FastAPI server:**
	```powershell
	uvicorn main:app --reload
	```
	The backend will be available at `http://127.0.0.1:8000`.

---

## Frontend Setup (React + Vite)

1. **Navigate to the frontend folder:**
	```powershell
	cd frontend
	```
2. **Install dependencies:**
	```powershell
	npm install
	```
3. **Start the development server:**
	```powershell
	npm run dev
	```
	The frontend will be available at `http://localhost:5173` by default.

---

## Connecting Frontend and Backend

- By default, the frontend and backend run on different ports. You may need to configure CORS in the backend (`main.py`) to allow requests from the frontend.
- Update API URLs in the frontend to point to the backend server (e.g., `http://127.0.0.1:8000`).

---

## Useful Scripts

- **Backend:**
  - `uvicorn main:app --reload` — Start FastAPI server with auto-reload
- **Frontend:**
  - `npm run dev` — Start Vite development server

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


