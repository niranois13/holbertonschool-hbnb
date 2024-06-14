# Project HBNB

## Description

This project is a part of the curriculum at HolbertonSchool. 
We were asked to create a crude replcia of an Airbnb styled application, focusing, for now, on the API in itself: POST data ; GET data ; PUT (update) data ; DELETE data from a "database" of JSON files, through HTTP requests.

This tas aims at improving our knowledge and getting hands-on experience with the following technologies, packages and modules:
- Python 3.10.12 for the coding language,
- Flask and GUnicorn to handle our application's RESTful API
- Unittest for, well, testing
- Docker for contanerization and persistence

To be more tangible, someone that uses our API will be able to create, update and delete a new user. Add (modify or delete) a new place for rental. Create (modify or delete) amenities for his place. Finally, a user can also post, update or delete reviews about places he doesn't own.

## Future implementations

In the future, our simple API will get improved with the following features:
- A real Database, with SQL (probably SQLAlchemy)
- A real security system, wth autorizations, authentification, etc.
- A proper front end, with HTML, CSS and JavaScript
- Many more


## Running the Docker Container

By default, the application runs on port 5000 using Gunicorn. If you need to run the application on a different port, you can override the `PORT` environment variable when starting the container.

### Example: Running on Port 8080

To run the application on port 8080, use the following command:

```sh
docker run -p 8080:8080 -e PORT=8080 myapp

