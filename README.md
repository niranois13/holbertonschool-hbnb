Le meilleur projet HBNB, par les meilleurs, pour les meilleurs. Que des villas avec piscine ici !

## Running the Docker Container

By default, the application runs on port 5000 using Gunicorn. If you need to run the application on a different port, you can override the `PORT` environment variable when starting the container.

### Example: Running on Port 8080

To run the application on port 8080, use the following command:

```sh
docker run -p 8080:8080 -e PORT=8080 myapp

