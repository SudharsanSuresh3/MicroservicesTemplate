# nameko_service/Dockerfile

# Use Python as base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /service

# Copy the current directory contents into the container
COPY . /service

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for the Nameko service
EXPOSE 8000

# Command to start the Nameko service
CMD ["nameko", "run", "--config", "./config/nameko_config.yaml", "nameko_service"]
