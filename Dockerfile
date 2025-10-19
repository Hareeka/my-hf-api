# Use a Python base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the default port for Hugging Face Spaces
EXPOSE 7860

# Command to run the application using Uvicorn
# The format is: uvicorn <module>:<variable> --host <host> --port <port>
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]