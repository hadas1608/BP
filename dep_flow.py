import os
import urllib
import tarfile
import requests

images = '/public/images'
if not os.path.exists(images):
    os.makedirs(images)
urllib.urlretrieve("http://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz", "/tmp/pandapics.tar.gz")
tar = tarfile.open("/tmp/pandapics.tar.gz")
tar.extractall(path=images)
tar.close()
os.system('docker-compose up -d')
health_request = requests.get('http://localhost:3000/health')
if health_request.status_code != 200:
    print "deployment flow failed, starting to kill the dockers"
    os.system('docker kill ops-exercise_web_1')
    os.system('docker kill ops-exercise_db_1')
