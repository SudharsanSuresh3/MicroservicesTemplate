# app/Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8010 available to the world outside this container
EXPOSE 8010

# Run the FastAPI app with Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8010"]
