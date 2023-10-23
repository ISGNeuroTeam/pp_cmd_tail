# Use an official Python runtime as a parent image
FROM python:3.9.7

# Describe credits
LABEL authors="mashida"

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

## Install virtualenv
#RUN python -m ensurepip --upgrade && \
#    pip install --upgrade pip && \
#    pip install virtualenv

# Create and setup venv
#ENV VIRTUAL_ENV=/app/venv
#RUN python -m venv $VIRTUAL_ENV
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"
#RUN echo $PATH

# Copy reqiurements
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --extra-index-url http://s.dev.isgneuro.com/repository/ot.platform/simple --trusted-host s.dev.isgneuro.com postprocessing-sdk
RUN pip install --no-cache-dir  -r requirements.txt

# Copy source code
COPY . /app

# Run tests
ENTRYPOINT ["pytest"]
