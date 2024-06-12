FROM python:3.11-alpine

# Update and install packages, create a user
RUN apk update && apk upgrade && \
    adduser -D -s /bin/bash hbnb

# Switch to the hbnb user and move to the /home/hbnb directory
USER hbnb
WORKDIR /home/hbnb

# Create the data directory in the user's directory
RUN mkdir hbnb_data

# Install Python dependencies from requirements.txt file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files into the container
COPY app ./app

# Define the Docker named volume "hbnb_data"
VOLUME [ "hbnb_data" ]

# Define environment variable for the port
ENV PORT 5000

# Expose the port for the application to be accessible
EXPOSE 5000

# Define the entry point of the application
WORKDIR /home/hbnb/app
CMD ["python", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

