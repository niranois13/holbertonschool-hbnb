FROM python:3.11

# Update and install packages, create a user
RUN apt-get update && apt-get upgrade -y && \
    useradd -ms /bin/bash hbnb

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

# Expose port 8080 for the application to be accessible
EXPOSE 8080

# Define the entry point of the application
ENTRYPOINT [ "python", "/home/hbnb/app/app.py" ]
