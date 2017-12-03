FROM ubuntu
MAINTAINER Julien Delange <julien@gunnm.org>
RUN apt-get update -y
RUN apt-get install -y python3 python-pip-whl python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN rm -f app.db
RUN python3 ./db_create.py
EXPOSE 5050
ENTRYPOINT ["python3"]
CMD ["run-production.py"]
