import os
import urllib
import tarfile
import requests
import time

images = '/public/images'
if not os.path.exists(images):
    os.makedirs(images)
urllib.urlretrieve("http://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz", "/tmp/pandapics.tar.gz")
tar = tarfile.open("/tmp/pandapics.tar.gz")
tar.extractall(path=images)
tar.close()
os.system('docker-compose up -d')
#sleeping for 10 seconds, waiting for the web server to start
time.sleep(10)
health_request = requests.get('http://localhost:3000/health')
if health_request.status_code != 200:
    print "deployment flow failed, killing the containers"
    os.system('docker kill ops_web')
    os.system('docker kill ops_db')
else:
    print "deployment flow succeeded!"
