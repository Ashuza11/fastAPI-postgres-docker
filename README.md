# CURDE API Using Postgres DB and Docker

## Project Overview

This project is a CRUD API built with FastAPI, using PostgreSQL as the database and Docker for containerization. It provides endpoints to Create, Read, Update, Delete, and Execute operations on data.

## Features

- FastAPI for building the API
- PostgreSQL for database management
- Docker for containerization
- CRUD operations

## Prerequisites

- Docker
- Docker baisc commands

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:Ashuza11/fastAPI-postgres-docker.git
   cd your-repo
   ```

2. Create a `.env` file and configure your environment variables:

   ```env
   POSTGRES_USER=yourusername
   POSTGRES_PASSWORD=yourpassword
   POSTGRES_DB=yourdatabase
   ```

3. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

## Usage

Access the API documentation at `http://localhost:8000/docs` to interact with the endpoints.

## Endpoints

- `GET /items/` - Retrieve all contacts
- `GET /items/{id}` - Retrieve an contact by ID
- `POST /items/` - Create a new contact
- `PUT /items/{id}` - Update an contact by ID
- `DELETE /items/{id}` - Delete an contact by ID

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
