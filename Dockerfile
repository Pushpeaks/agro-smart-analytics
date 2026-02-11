# --- Stage 1: Build the React Frontend ---
FROM node:18-alpine as build-frontend
WORKDIR /agro-frontend
COPY agro-frontend/package*.json ./
RUN npm install
COPY agro-frontend/ ./
RUN npm run build

# --- Stage 2: Setup the Python Backend ---
FROM python:3.10-slim
WORKDIR /code

# Install system dependencies (needed for some ML libs)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create app directory structure
RUN mkdir -p app/services app/routes app/utils app/models

# Copy the backend code
COPY app/ ./app/

# Copy the built frontend from Stage 1
COPY --from=build-frontend /agro-frontend/build ./agro-frontend/build

# Expose port 7860 (Hugging Face default)
EXPOSE 7860

# CMD to run the backend (which also serves the frontend)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
