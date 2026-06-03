# 🎬 BingeBuddy – Movie Recommendation System

## 📌 Project Overview

BingeBuddy is a movie recommendation system developed using Python, Django, SQLite, Tkinter, HTML, and CSS. The application recommends movies based on user preferences such as mood, companion type, language, genre, and year range.

The project provides both:

* 🌐 Web-based GUI using Django
* 🖥️ Desktop GUI using Tkinter

Both interfaces use the same movie database and recommendation logic.

---

## 🚀 Features

* Multi-step interactive movie recommendation quiz
* Personalized movie suggestions
* Mood-based recommendations
* Genre-based filtering
* Companion-based recommendations
* Language preferences
* Year-range selection
* Movie poster integration using OMDb API
* Poster processing using OpenCV
* Modern animated user interface
* SQLite database integration
* Tkinter desktop version

---

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS
* Django Templates

### Backend

* Python
* Django Framework

### Database

* SQLite3
* Django ORM

### GUI

* Django Web GUI
* Tkinter Desktop GUI

### Additional Libraries

* OpenCV
* Requests
* Pandas

---

## 📂 Project Structure

```text
BingeBuddy/
│
├── bingebuddy_config/
├── recommender_app/
├── templates/
├── static/
├── dataset/
├── db.sqlite3
├── manage.py
├── bingebuddy_desktop.py
└── requirements.txt
```

---

## ⚙️ Recommendation Logic

The recommendation engine compares user preferences with movie attributes stored in the database.

Matching criteria:

* Mood
* Genre
* Language
* Companion Type
* Year Range

Each matching attribute increases the movie score.

Movies are ranked based on:

1. Matching Score
2. Movie Rating

The top 3 highest-ranked movies are displayed to the user.

---

## 🗄️ Database Design

Movie records contain:

* Title
* Genre
* Language
* Mood
* Companion Type
* Year Range
* Rating
* Poster URL

Database is implemented using SQLite and managed through Django ORM.

---

## 🎯 Python Concepts Used

* Functions
* Conditional Statements
* Loops
* Lambda Functions
* List Processing
* File Handling
* Object-Oriented Programming
* Classes and Objects
* Exception Handling
* Session Management
* API Integration
* Database Operations
* Image Processing

---

## 🖥️ Running the Django Application

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🖥️ Running the Tkinter Application

```bash
python bingebuddy_desktop.py
```

---

## 👨‍💻 Developed By

Ayesha Shaikh

---

## 📚 Academic Purpose

This project was developed as part of the Application Programming Laboratory (APP Lab) course to demonstrate GUI development, database integration, recommendation systems, API usage, image processing, and web application development using Python.

