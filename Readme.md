## Build the container using

```
docker build --platform linux/arm64 -t ccs-extractor .
```

## Run the container using

```
docker run -e AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY> -e AWS_SECRET_ACCESS_KEY=<YOUR_SECRET> -e AWS_DEFAULT_REGION=us-east-1 ccs-extractor
```

## Library used

https://aws-samples.github.io/amazon-textract-textractor/index.html

