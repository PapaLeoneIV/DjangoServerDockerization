FROM python:3.12-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
# Copy the current directory contents into the container at /app

# Correct the path and ensure the script is executable
# Run Django application
CMD ["/bin/sh", "-c", "chmod +x /app/services/django/script.sh && /app/services/django/script.sh"]