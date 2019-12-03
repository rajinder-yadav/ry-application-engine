# Cloud Run Setup

```sh
gcloud auth login
gcloud config set project <project-id>
```

```sh
gcloud config list
gcloud auth list
```

Trouble shooting

You want to use "__GOOGLE_APPLICATION_CREDENTIALS__" when working through a Service Account, otherwise unset it.
```
gcloud auth application-default revoke
echo $GOOGLE_APPLICATION_CREDENTIALS

unset GOOGLE_APPLICATION_CREDENTIALS
```

Work with your User account Permissions.

- [gcloud auth application-default login](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login)

```
gcloud auth application-default login
```

1. Enable Cloud Run API
1. Enable Cloud Build API
1. Add Role to create Storage Buckets (role/admin)

- [Docker - Container runtime contract](https://cloud.google.com/run/docs/reference/container-contract)

- By default, container instances can scale up to 1000 instances. For more requires a quota increase.
- By default Cloud Run container instances can receive many requests at the same time (up to a maximum of 80).

To minimize the impact of cold starts, Cloud Run may maintain a reserve of idle container instances for your revision. These instances are ready to handle requests in case of a sudden traffic spike. Note that for Cloud Run (fully managed), you are not billed for this.

An idle container instance may persist resources, such as open database connections. However, for Cloud Run (fully managed), the CPU will not be available

Cloud Run allocates 1 vCPU per container instance, and this cannot be changed. A vCPU is implemented as an abstraction of underlying hardware to provide the approximate equivalent CPU time of a single hardware hyper-thread on variable CPU platforms. The container instance may be executed on multiple cores simultaneously.


## Building Docker Image and pushing it up to GCR

https://documentation.suse.com/sles/15-SP1/html/SLES-all/book-sles-docker.html

```sh
gcloud builds submit --tag gcr.io/raj-cloud-run/nodeapp
gcloud beta run deploy --image gcr.io/raj-cloud-run/nodeapp --platform managed --memory 1024Mi


curl -X GET https://nodeapp-erszkvwila-uc.a.run.app/data
ab -n 300 -c 10 https://nodeapp-erszkvwila-uc.a.run.app/data
```

gcloud builds submit --tag gcr.io/piktv-purchchanrecomm-797785d7/nodeapp
gcloud beta run deploy --image gcr.io/piktv-purchchanrecomm-797785d7/nodeapp --platform managed --memory 1024Mi

```sh
gcloud auth configure-docker
docker run -d --rm --name app -p 8080:8080 gcr.io/raj-cloud-run/nodeapp

PORT=8080 docker run -d --rm --name app -p 8080:${PORT} -e PORT=${PORT} gcr.io/raj-cloud-run/nodeapp/cloudrun-test
```

https://github.com/putztzu/docker/blob/master/docs/installation/linux/SUSE.md


Local build and testing.

```sh
docker build -t yadav/nodeapp --no-cache .
docker run -d --rm --name nodeapp -p 8080:8080 yadav/nodeapp
docker stop app
```
