# Python Web Server

- [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)
- [Docker - Container runtime contract](https://cloud.google.com/run/docs/reference/container-contract)

## Start a Virtual Environment

```sh
python3 -m venv venv
source ./venv/bin/activate
```

### Install Flash

```sh
pip install Flask
```

## Saving Requirements

This will save all the requrement in the current environment.

```sh
pip freeze > requirements.txt
```

## Install Requirements

pip install -r requirements.txt

## Run App

```sh
python app.py
```

## Build Docker Container

```sh
docker build -t yadav/pyapp --no-cache .
docker run --rm -d -p 8080:8080 --name pyapp yadav/pyapp
```

## Cloud Run Setup

- [Docker - Container runtime contract](https://cloud.google.com/run/docs/reference/container-contract)

- By default, container instances can scale up to 1000 instances. For more requires a quota increase.
- By default Cloud Run container instances can receive many requests at the same time (up to a maximum of 80).

To minimize the impact of cold starts, Cloud Run may maintain a reserve of idle container instances for your revision. These instances are ready to handle requests in case of a sudden traffic spike. Note that for Cloud Run (fully managed), you are not billed for this.

An idle container instance may persist resources, such as open database connections. However, for Cloud Run (fully managed), the CPU will not be available

Cloud Run allocates 1 vCPU per container instance, and this cannot be changed. A vCPU is implemented as an abstraction of underlying hardware to provide the approximate equivalent CPU time of a single hardware hyper-thread on variable CPU platforms. The container instance may be executed on multiple cores simultaneously.


## Building Docker Image and pushing it up to GCR

https://documentation.suse.com/sles/15-SP1/html/SLES-all/book-sles-docker.html

```sh
gcloud builds submit --tag gcr.io/raj-cloud-run/pyapp
gcloud run deploy --image gcr.io/raj-cloud-run/pyapp --platform managed --memory 1024Mi

curl -X GET https://nodeapp-erszkvwila-uc.a.run.app/data
ab -n 300 -c 10 https://nodeapp-erszkvwila-uc.a.run.app/data
```

gcloud builds submit --tag gcr.io/piktv-purchchanrecomm-797785d7/pyapp
gcloud run deploy --image gcr.io/piktv-purchchanrecomm-797785d7/pyapp --platform managed --memory 1024Mi


gcloud builds submit --tag gcr.io/raj-cloud-run-gke/pyapp
gcloud run deploy --image gcr.io/raj-cloud-run-gke/pyapp --platform gke --cluster ry-cluster --cluster-location us-central1-b --memory 1024Mi


```sh
gcloud auth configure-docker
docker run -d --rm --name app -p 8080:8080 gcr.io/raj-cloud-run/pyapp

PORT=8080 docker run -d --rm --name app -p 8080:${PORT} -e PORT=${PORT} gcr.io/raj-cloud-run/pyapp
```

https://github.com/putztzu/docker/blob/master/docs/installation/linux/SUSE.md


Local build and testing.

```sh
docker build -t yadav/pyapp --no-cache .
docker run -d --rm --name pyapp -p 8080:8080 yadav/pyapp
docker stop app
```
