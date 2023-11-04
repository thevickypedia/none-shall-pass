FROM ubuntu:latest

RUN apt-get update && apt-get install -y git

COPY src/run.sh /run.sh

RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
