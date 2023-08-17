FROM python:3.9-slim-buster as build

# Set the environment variable for the bot name
ENV BOT_NAME=$BOT_NAME

# Set the working directory in the container
WORKDIR /usr/src/app/"${BOT_NAME}"

COPY requirements.txt /usr/src/app/"${BOT_NAME}"
RUN pip install --upgrade pip
RUN pip install -r /usr/src/app/"${BOT_NAME}"/requirements.txt

FROM python:3.9-slim-buster

# Set the environment variable for the bot name
ENV BOT_NAME=$BOT_NAME

# Set the working directory in the container
WORKDIR /usr/src/app/"${BOT_NAME}"

# Copy the installed dependencies from the first stage to the second stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

COPY . /usr/src/app/"${BOT_NAME}"
