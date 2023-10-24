# Use an official Python runtime as a parent image
FROM python:3.9.7

# Describe credits
LABEL authors="mashida"

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

# Set the working directory
WORKDIR /app

# Copy reqiurements
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --disable-pip-version-check --no-cache-dir --extra-index-url http://s.dev.isgneuro.com/repository/ot.platform/simple --trusted-host s.dev.isgneuro.com postprocessing-sdk
RUN pip install --disable-pip-version-check --no-cache-dir  -r requirements.txt

# Copy source code
COPY . /app

# Copy readFile config.ini
COPY tests/config.ini  /usr/local/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini

# Run tests
ENTRYPOINT ["pytest"]
