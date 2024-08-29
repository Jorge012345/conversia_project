# CONVERSIA NOTIFICATION API

## Overview
This is a FastAPI-based server for managing notifications across various communication channels, such as SMS, email, and push notifications.

## Requirements
- Python 3.9+
- Docker

## Usage

### Local Development
To run the server locally, please execute the following from the root directory:

1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the FastAPI server:
    ```sh
    uvicorn main:app --reload --port 8000
    ```

3. Open your browser and navigate to:
    ```
    http://localhost:8000/docs
    ```
    Here you can view and interact with your API using the Swagger UI.

### Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

1. Build the Docker image:
    ```sh
    docker build -t conversia .
    ```

2. Start a Docker container:
    ```sh
    docker run -p 8000:8000 conversia
    ```

3. Open your browser and navigate to:
    ```
    http://localhost:8000/docs
    ```
    Here you can view and interact with your API using the Swagger UI.

## Authentication

### Generating Access Tokens

The API uses Bearer Token authentication for secure access. Each police officer is associated with an access token which needs to be generated and included in the headers of POST requests.

#### Generating a Token via API

To generate an access token, make a POST request to the `/auth/v1/token` endpoint with the officer's ID. Here is an example using `curl`:

```sh
curl -X POST "http://localhost:8000/auth/v1/token" \
-H "accept: application/json" \
-H "Content-Type: application/json" 
```


## Additional Information

- The API documentation is available at `/docs` once the server is running.
- The OpenAPI schema is available at `/openapi.json`.