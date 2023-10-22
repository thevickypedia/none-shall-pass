# Stage 1: Download the file
FROM alpine AS downloader
RUN apk --no-cache add curl
RUN curl -o /validator.py https://raw.githubusercontent.com/thevickypedia/none-shall-pass/main/src/validator.py

# Stage 2: Create the final image
FROM python:3.11-alpine
COPY --from=downloader /validator.py /validator.py
RUN chmod +x /validator.py
ENTRYPOINT ["python", "/validator.py"]
