FROM python:3.11-slim

WORKDIR /app

# Copy requirements first
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project including client/
COPY . /app

# Expose port from .env (default 80)
EXPOSE 80

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
