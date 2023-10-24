# Pull python3.11-alpine image (smallest)
FROM python:3.11-alpine

# Install git
RUN apk add --no-cache git

# Copy package data to root
COPY src/* /

# Upgrade pip and install requests module
RUN python -m pip install --upgrade pip
RUN python -m pip install requests

# Set validator.py as executable
RUN chmod +x /validator.py

# Set entrypoint for docker run
ENTRYPOINT ["python", "/validator.py"]
