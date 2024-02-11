# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install poetry
RUN pip install poetry

# Use poetry to install dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Expose the port the app runs in
EXPOSE 8000

# Define the command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
