FROM python:3.8.6-slim-buster

#RUN mkdir /myfirstdockerapp
WORKDIR /myfirstdockerapp
COPY . .
#RUN cp server_settings.py local_settings.py
RUN pip3 install -r requirements.txt
CMD python3 manage.py runserver 0.0.0.0:8000
