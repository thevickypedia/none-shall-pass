# Pull python3.11-alpine image (smallest)
FROM python:3.11-alpine

# Install git
RUN apk add --no-cache git

# Create a new directory in root and copy the module
RUN mkdir /none-shall-pass
COPY . /none-shall-pass

# Upgrade pip and install requests module
RUN python -m pip install --upgrade pip
RUN python -m pip install requests

# Set working directory
WORKDIR /none-shall-pass

# Set entrypoint for docker run
ENTRYPOINT ["python", "./src/validator.py"]
