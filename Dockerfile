FROM ubuntu:latest

RUN apk add --no-cache git

COPY src/run.sh /run.sh

RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
