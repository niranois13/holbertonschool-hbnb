FROM python:3.11-alpine

# Update and install packages, create a user
RUN apk update && apk upgrade && \
    adduser -D -s /bin/bash hbnb

# Create the data directory in the user's directory as root
RUN mkdir -p /home/hbnb/hbnb_data

# Copy data files into the container with the correct ownership and permissions as root
COPY data/* /home/hbnb/hbnb_data/
RUN chown -R hbnb:hbnb /home/hbnb/hbnb_data && chmod -R 777 /home/hbnb/hbnb_data

# Switch to the hbnb user and set the working directory
USER hbnb
WORKDIR /home/hbnb

# Copy Python dependencies from requirements.txt file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files into the container
COPY app ./app

# Define the Docker named volume "hbnb_data"
VOLUME ["/home/hbnb/hbnb_data"]

# Define environment variable for the port
ENV PORT 5000

# Expose the port for the application to be accessible
EXPOSE 5000

COPY app/data hbnb_data

# Define the entry point of the application
WORKDIR /home/hbnb/app
CMD ["python", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
