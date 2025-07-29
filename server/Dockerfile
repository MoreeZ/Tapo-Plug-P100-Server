# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies if needed
# RUN apt-get update && apt-get install -y ...

# Copy project files
COPY . /app

# Install dependencies if you have requirements.txt
# If not, skip this step
# RUN pip install --no-cache-dir -r requirements.txt

# Install python-dotenv to load env variables
RUN pip install python-dotenv

# Expose port (use the one from your .env, default 80)
EXPOSE 80

# Run the application
CMD ["python", "main.py"]
