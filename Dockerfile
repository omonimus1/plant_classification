FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc

ADD requirements.txt requirements.txt
# . ADD export.pkl export.pkl
# . ADD saved_model.pb  saved_model.pb 
ADD app.py app.py

# Install required libraries
RUN pip install -r requirements.txt

# Run it once to trigger resnet download
RUN python app.py

EXPOSE 8008

# Start the server
CMD ["python", "app.py", "serve"]