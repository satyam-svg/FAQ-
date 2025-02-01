# Use an official Python runtime as base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (Improves Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
