# Use Python Alpine base image
FROM python:latest

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt ./
COPY app.py ./

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8501

# Command to run the Streamlit app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
