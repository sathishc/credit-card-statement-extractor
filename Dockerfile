FROM --platform=linux/amd64 public.ecr.aws/docker/library/python:3.10
LABEL maintainer="Sathish H"
RUN apt-get update
RUN apt-get install poppler-utils -y
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY main.py ./
CMD ["python3", "main.py"]