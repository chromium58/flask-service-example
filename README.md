### EXAMPLE. Simple python(flask) service example

### RUN App in Docker

1. Clone repo

2. ```docker build -t flask-service-example . ```

3. ```docker run -p 8080:8080 -e APP_SETTINGS=development flask-service-example```

### OR run it simply with python

1. Clone repo

2. ```pip3 install -r requirements.txt```

3. ```APP_SETTINGS=development python3 run.py```

### Check if it works -

Check API Swagger in browser - http://127.0.0.1/api/swagger

Or using curl:

```
$ curl -X POST -H "Content-Type: application/json" -d '{"city": "Moscow"}' http://127.0.0.1:8080/api/test
{
    "result": "Today in Moscow: 🌨  +30°C"
}
```
### TESTS

This example has unit and integration tests.

Unit tests are located in app/tests/controllers
Unit tests are simple, they check our API by mocking external wttr.in website in our case.

Integration tests are located in app/tests/resources

These are more complex, they running fake server which simulates response of wttr.in, so tests making real HTTP calls to our API.

How to run tests:

1. Close this repo

2. ```pip3 install tox```

3. ```tox```
