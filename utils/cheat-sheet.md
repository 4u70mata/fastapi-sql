# Intro 
  
This cheat sheet covers essential tasks and components for working with FastAPI, SQLAlchemy, and RESTful API best practices. Keep this handy for quick reference, especially before your interview. If you have more specific topics or questions, feel free to ask!  
### FastAPI Cheat Sheet

| **Task**                   | **Code Snippet**                                           | **Description**                                             |
|----------------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| Create a FastAPI app       | `from fastapi import FastAPI` <br> `app = FastAPI()`   | Initializes a FastAPI application.                          |
| Define a GET endpoint      | `@app.get("/items/{item_id}")` <br> `def read_item(item_id: int): return {"item_id": item_id}` | Creates a GET endpoint that returns item details.          |
| Define a POST endpoint     | `@app.post("/items/")` <br> `def create_item(item: Item): return item` | Creates a POST endpoint to create a new item.              |
| Dependency Injection        | `def get_db(): ...` <br> `db: Session = Depends(get_db)` | Provides a database session to route handlers.              |
| Request Body Validation     | `class Item(BaseModel): name: str; price: float` <br> `@app.post("/items/")` | Validates incoming request data using Pydantic models.     |
| Response Model              | `class ItemResponse(BaseModel): id: int; name: str` <br> `@app.get("/items/{item_id}", response_model=ItemResponse)` | Specifies the response model for the endpoint.             |
| CORS Middleware             | `from fastapi.middleware.cors import CORSMiddleware` <br> `app.add_middleware(CORSMiddleware, allow_origins=["*"])` | Enables CORS for your FastAPI app.                         |

### SQLAlchemy Cheat Sheet

| **Task**                       | **Code Snippet**                                               | **Description**                                             |
|--------------------------------|---------------------------------------------------------------|-------------------------------------------------------------|
| Create an Engine               | `from sqlalchemy import create_engine` <br> `engine = create_engine(DATABASE_URL)` | Initializes a database connection engine.                  |
| Create a Session               | `from sqlalchemy.orm import sessionmaker` <br> `SessionLocal = sessionmaker(bind=engine)` | Creates a new session for interacting with the database.   |
| Define a Model                 | `class User(Base): __tablename__ = "users"; id = mapped_column(primary_key=True)` | Defines a database model.                                   |
| Create Tables                  | `Base.metadata.create_all(bind=engine)`                     | Creates all tables defined by the models in the database.  |
| Query All Records              | `users = db.query(User).all()`                               | Retrieves all records from the User table.                 |
| Add a Record                   | `db.add(new_user)` <br> `db.commit()`                       | Adds a new record to the database.                         |
| Update a Record                | `db_user.name = "new name"` <br> `db.commit()`              | Updates an existing record.                                 |
| Delete a Record                | `db.delete(db_user)` <br> `db.commit()`                     | Deletes a record from the database.                         |

### RESTful API Best Practices

| **Principle**                | **Guideline**                                               | **Example**                                                  |
|------------------------------|------------------------------------------------------------|--------------------------------------------------------------|
| Use Nouns for Resource URLs   | Use nouns for endpoints to represent resources.            | `/users`, `/items`, `/products`                             |
| Use HTTP Methods              | Use appropriate HTTP methods for CRUD operations.         | GET for retrieving, POST for creating, PUT for updating, DELETE for removing. |
| Status Codes                  | Use standard HTTP status codes for responses.             | 200 OK, 201 Created, 204 No Content, 400 Bad Request, 404 Not Found, 500 Internal Server Error |
| Versioning                    | Version your API using URL or headers.                    | `/v1/users`, `/api/v2/items`                               |
| Pagination                    | Implement pagination for large datasets.                   | Use query parameters like `?page=1&limit=10`                |
| Filtering and Sorting         | Allow filtering and sorting of resources.                  | `/items?sort=price&filter=available`                       |

### Common Commands

| **Task**                       | **Command**                                                 | **Description**                                             |
|--------------------------------|------------------------------------------------------------|-------------------------------------------------------------|
| Run FastAPI with Uvicorn       | `uvicorn main:app --reload`                               | Starts the FastAPI server in development mode.             |
| Create a virtual environment    | `python -m venv venv`                                    | Creates a virtual environment for your project.            |
| Activate virtual environment     | `source venv/bin/activate` (Linux/Mac) <br> `venv\Scripts\activate` (Windows) | Activates the virtual environment.                          |
| Install dependencies            | `pip install -r requirements.txt`                         | Installs the listed packages in `requirements.txt`.        |
