FROM python:3.12-slim-bullseye

# Set the working directory

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container

EXPOSE 8000

# Define environment variable

ENTRYPOINT ["uvicorn", "src.main:app", "--host", "localhost", "--port", "8000"]