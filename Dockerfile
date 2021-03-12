FROM python:3.7

COPY main.py /
COPY flaskroutes.py /
COPY utilities.py /
COPY pictures.py /
COPY tables.py /
COPY texte.py /

RUN pip3 install flask
RUN pip3 install setuptools
RUN pip3 install pathlib
RUN pip3 install celery
RUN pip3 install pillow
RUN pip3 install python-magic
RUN pip3 install libmagic
RUN pip3 install filetype
RUN pip3 install boto3
RUN pip3 install pandas
RUN pip3 install PyPDF2

CMD [ "python3", "./main.py", "25252"  ]