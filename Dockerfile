FROM python:3.7

COPY requirements.txt /
COPY auth /

COPY main.py /
COPY flaskroutes.py /
COPY utilities.py /
COPY pictures.py /
COPY tables.py /
COPY texte.py /
COPY rekognition_objects.py /

RUN pip3 install -r requirements.txt

CMD [ "python3", "./main.py", "5555"  ]