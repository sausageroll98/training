# Use the ubuntu_miniconda_df as the base image
FROM python:3.8.12-slim

# Install flask and waitress
RUN pip install flask waitress

# Copy the python script containing the flask app from our host machine to the container
COPY ./hello_flask_app /hello_flask_app

# Change the directory to the hello_flask_app folder
WORKDIR /hello_flask_app

#Run the waitress-serve command
CMD ["waitress-serve","--host=0.0.0.0","--port=5050","hello_flask:app"]

