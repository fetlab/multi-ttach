# Use the latest official Python image
FROM python:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Update the system and install build-essential
RUN apt-get update && apt-get install -y build-essential cmake libopenblas-dev

RUN pip install --upgrade pip

COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code
COPY . .

# Define the command to run your application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

