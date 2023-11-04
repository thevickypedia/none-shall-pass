FROM alpine:3.14

RUN apk add --no-cache git

COPY src/run.sh /run.sh

RUN chmod +x /run.sh

ENTRYPOINT ["bash", "/run.sh"]
