# Init base image
FROM python:3.9-slim

# Create directories
RUN mkdir /app
RUN mkdir /app/models

# copy all the stuff to directory
ADD ./prediction_server /app
ADD ./requirements.txt /app

# copy the custom ml_models package
COPY ./ml_models.tar.gz /app

# run pip to install dependencies
RUN pip install /app/ml_models.tar.gz 
RUN pip install -r /app/requirements.txt

# remove custom package
RUN rm /app/ml_models.tar.gz

# Run server
CMD ["python", "-m", "app"]