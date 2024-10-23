# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Command to run the Django app using Gunicorn
CMD ["gunicorn", "hyperion.wsgi:application", "--bind", "0.0.0.0:8000"]
