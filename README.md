# 🎵 Voting System for Music Club – Ala-Too International University

This project is a secure and user-friendly **Voting System** developed for electing the **President of the Music Club** at **Ala-Too International University**. It allows students from both the **University and College divisions** to vote once using their **ID card number**.

---

## 📌 Project Features

- **Secure Login System**  
- **One-Time Voting Restriction** (based on student ID)  
- **Fixed Candidates** (4 candidates pre-registered in the database)  
- **Modern GUI with PyQt6**  
- **MVC Architecture**  
- **SQLite Database**  
- **Custom Notifications for Errors and Success**  
- **Basic Unit Testing for Core Logic**

---

## 🧱 Technology Stack

- `Python 3.10+`  
- `PyQt6`  
- `SQLite3`  
- `Figma` (for UI design prototype)  
- `unittest` (for testing)

---

## 🗂️ Project Structure

```
project/
├── models/          # Model: Data logic, DAO classes
│   ├── candidate.py
│   ├── student.py
│   └── vote.py
├── views/           # View: PyQt6 UI files
│   └── main_window.ui
├── controller/      # Controller: App logic & interaction
│   └── main.py
├── database/        # SQLite database + init script
│   └── voting.db
├── tests/           # Unit tests
│   └── test_vote.py
└── README.md
```

---

## 📊 Database

- **Tables:**
  - `students` – contains student IDs
  - `candidates` – 4 predefined candidates
  - `votes` – stores who voted for whom

- **DAO Classes:**  
  Used to perform all Create, Read, Update, Delete operations.

- **Reports (Examples):**
  - Total votes per candidate
  - Who has voted
  - Who hasn't voted
  - Voter turnout percentage
  - Most popular candidate

---

## 🧪 Testing

Basic unit tests are provided for:
- Recording votes
- Ensuring a student can’t vote more than once
- Verifying vote count accuracy

---

## ✨ Authors

- **Venera [You]**
- **Your Teammate’s Name**  
*Ala-Too International University – 2025*
