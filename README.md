# 📝 To-Do List CLI App (with JSON storage & multi-user login)

A simple command-line To-Do List application built with Python. This app allows users to register or log in, add and manage tasks, mark importance, and include extra notes. Data is persistently stored using a JSON file.

---

## 📌 Features

- ✅ Register and login system (with JSON-based user management)
- 🧠 Add todos with descriptions, importance flags, and optional notes
- 👀 View all todos, including a detailed display mode
- ✏️ Edit todos by field (name, description, importance, notes)
- ❌ Delete individual or all todos
- 💾 Data is saved in a structured JSON format (`db.json`)
- 💻 Built fully using core Python (no external libraries except `json`)

---

## 🧰 Tech Stack

- Python 3.x
- JSON file for persistent storage
- No external dependencies

---

## 🚀 How to Run

1. Clone the repository:
bash
git clone https://github.com/PromptoZ9/todo-list-app.git
cd todo-list-app

2. Make sure db.json exists. If not, create an empty file like this:
   {}

3. Run the Script:
   python todo_app.py

👥 User Flow
1. Register or Login

2. Choose from menu:

   - Add Todo

   - See Todos

   - Edit Todo

   - Delete Todo

   - Delete All Todos

   - Exit

3. Your data is saved in db.json under your username.




📂 File Structure

todo_app.py          # Main application logic
db.json              # JSON database for storing user & todo data
README.md            # This file

📄 License
This project is open-source and intended for educational/personal use.

🔗 Author
Made with ❤️ by PromptoZ9


