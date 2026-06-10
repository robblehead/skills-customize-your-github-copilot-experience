# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using FastAPI by creating endpoints, validating request and response data, and handling errors. Students will build a small task manager API that supports common CRUD operations.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Endpoints

#### Description
Set up a FastAPI app and create basic endpoints to check that the API is running and to list tasks from an in-memory collection.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Add a `GET /` endpoint that returns a welcome message.
- Add a `GET /tasks` endpoint that returns a list of task objects.
- Start the API with Uvicorn and verify both endpoints in the browser or API docs.


### 🛠️ Implement Task CRUD Operations

#### Description
Add endpoints for creating, updating, and deleting tasks. Use Pydantic models to validate input data.

#### Requirements
Completed program should:

- Define a Pydantic model for task input with `title` and optional `completed` fields.
- Add a `POST /tasks` endpoint to create a new task with an auto-generated `id`.
- Add a `PUT /tasks/{task_id}` endpoint to update an existing task.
- Add a `DELETE /tasks/{task_id}` endpoint to remove a task.
- Return appropriate JSON responses after each operation.


### 🛠️ Add Error Handling and Testing with API Docs

#### Description
Improve reliability by returning proper HTTP status codes when tasks are not found and test all routes with FastAPI's built-in interactive docs.

#### Requirements
Completed program should:

- Return `404` when a task ID does not exist.
- Return `201` when creating a task successfully.
- Include clear error messages in JSON format.
- Test all endpoints using `/docs` and confirm expected behavior.
