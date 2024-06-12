FROM python:3.11-alpine

# Update and install packages, create a user
RUN apk update && apk upgrade && \
    adduser -D -s /bin/bash hbnb

# Switch to the hbnb user and move to the /home/hbnb directory
USER hbnb
WORKDIR /home/hbnb

# Create the data directory in the user's directory
RUN mkdir hbnb_data

# Copy Python dependencies from requirements.txt file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files into the container
COPY app ./app

# Copy data files into the container
COPY --chown=hbnb:hbnb data/* /home/hbnb/hbnb_data/

# Define the Docker named volume "hbnb_data"
VOLUME ["hbnb_data"]

# Set permissions on the mounted volume
RUN chmod -R 777 /home/hbnb/hbnb_data

# Define environment variable for the port
ENV PORT 5000

# Expose the port for the application to be accessible
EXPOSE 5000

# Define the entry point of the application
WORKDIR /home/hbnb
CMD ["python3", "app/app.py"]
