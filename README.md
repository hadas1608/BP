I worked on an Ubuntu 14.04 with Python 2.7.6, docker and docker-compose.

In order to run the script run (from root directory of the repo): python dep_flow.py
please note i've added a container_name for both containers so i guess there is no chance the same containers names exist on your server, but in case there are already containers with those names and you are getting errors regarding an existing container with the same name please run:

docker stop ops_web
docker stop ops_db

docker rm ops_web
docker rm ops_db

and then run the script again.
