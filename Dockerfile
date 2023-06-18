# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /warehouse_bot

# Copy the current directory contents into the container at /warehouse_bot
COPY . /warehouse_bot

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 443

WORKDIR /warehouse_bot/app

# Run app.py when the container launches
CMD ["python", "app.py"]