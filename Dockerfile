# Use the official Python 3.11 image from the Docker Hub
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY pyproject.toml .

# Install any dependencies
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

# Copy the content of the local src directory to the working directory in Docker
COPY . .

# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
