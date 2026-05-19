
## 📌 Project Description

This is a REST API-based Book Management project built using Django REST Framework. The application allows users to manage book records by performing CRUD (Create, Read, Update, Delete) operations through API endpoints.

The project demonstrates how backend systems handle data flow between client and server using RESTful architecture. It focuses on building scalable and structured APIs for real-world applications.

---

## ⚙️ How It Works

The project follows a simple backend workflow:

1. **Client Request**  
   The user sends HTTP requests (GET, POST, PUT, DELETE) to the API endpoints.

2. **URL Routing**  
   Django routes the request to the appropriate view function based on the URL pattern.

3. **Views (Business Logic)**  
   The view processes the request and performs required operations like fetching, creating, updating, or deleting data.

4. **Models (Database Layer)**  
   Data is stored and managed in the database using Django models.

5. **Serializers (Data Conversion Layer)**  
   Serializers convert complex model data into JSON format and validate incoming data.

6. **Response**  
   The API returns structured JSON responses back to the client.

---

## 🛠️ Technologies Used

- Python 🐍  
- Django 🟢  
- Django REST Framework ⚡  
- SQLite Database 🗄️  

---

## 🎯 Key Features

- Full CRUD operations for books  
- RESTful API design  
- Data validation using serializers  
- JSON response handling  
- Clean backend architecture
---

## 📂 API Endpoints
- GET /api/books/ → List all books  
- POST /api/books/ → Create book  
- GET /api/books/{id}/ → Get single book  
- PUT /api/books/{id}/ → Update book  
- DELETE /api/books/{id}/ → Delete book  

---
## 🚀 Project Use

👉 This project can be used as a basic backend template for real-world applications and API development practice.

## 👨‍💻 Author
Gajullapalli Shashikala Reddy  
Email: reddyshashikala05@gmail.com  
