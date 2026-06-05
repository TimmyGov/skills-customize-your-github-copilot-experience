# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a small REST API using the FastAPI framework. You will practice creating endpoints, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI application and implement endpoints for managing a simple in-memory list of books. Your API should support creating and retrieving books.

#### Requirements
Completed program should:

- Create a FastAPI app in starter-code.py.
- Implement GET /health that returns {"status": "ok"}.
- Implement GET /books that returns a JSON array of all books.
- Implement POST /books that accepts a new book object and adds it to memory.
- Return HTTP status code 201 when a book is created successfully.


### 🛠️ Add Validation and Error Handling

#### Description
Improve the API by adding request validation and handling common errors. The API should reject invalid input and return clear responses.

#### Requirements
Completed program should:

- Use Pydantic models to validate required fields: id (int), title (str), and author (str).
- Reject duplicate id values when creating a new book.
- Return HTTP 400 with a clear error message for duplicate id values.
- Return HTTP 422 automatically for invalid request body types or missing required fields.
- Include at least one example request and response in comments to help test the API.
