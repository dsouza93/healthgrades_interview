# healthgrades_interview API
This repository contains my solution for a coding challenge for a Healthgrades interview. The outline of the project can be found [here](https://gist.github.com/andrewpuch/f8738feb0a38593744cb42b37caf39f4)

Here we have a very simple python Flask implementation of a RESTful API. The API will run on localhost and accept requests through port 3000. The API accepts all URIs and all HTTP Methods. The restful API running within the container will write to a log file on the Docker host, logging the HTTP method and URI. 

# Usage
Once you have pulled down the repository, simply use the command: 
```
make run
```
This will build and spawn a container running the application. Use a browser or the curl command to send requests to localhost:3000. The logs can be currently found in /tmp/logs/. 

# Useful Links:
[Flask Documentation](http://flask.pocoo.org/docs/0.12/)
[Potential Container Using Nginx/uwsgi](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)
