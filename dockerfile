FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY runpod_serverless/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY runpod_serverless/ ./runpod_serverless/
COPY runpod.yaml .
COPY deploy.py .

# Default entrypoint for RunPod serverless
ENV PYTHONUNBUFFERED=1
CMD ["python", "deploy.py"]