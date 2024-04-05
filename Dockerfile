# Base image for Python environment
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

RUN pip uninstall multipart -y
RUN pip install python-multipart
# Install dependencies
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# ENTRYPOINT [ "python", "/app/ingest.py" ]
EXPOSE 8080
# Command to run the application (replace 'main:app' with your actual entrypoint)
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8080"]