FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir /app && apt-get update && apt-get install -y \
	python3 \
	python3-pip \
	tzdata \
	libmariadb-dev \
	&& rm -rf /var/lib/apt/lists/*	

RUN pip3 install boto3 mariadb

WORKDIR /app

COPY ./db_script.py .
COPY ./S3_bucket.py .
COPY ./Db_operations.py .


CMD python3 db_script.py $ACCESSID $ACCESSKEY $USER $PASSWORD $HOST $PORT $DATABASE $TABLE $UPDATED $BUCKET 
