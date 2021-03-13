FROM python:3

ADD main.py /
ADD flaskroutes.py /
ADD settings.py /
ADD utilities.py /

RUN pip install flask
RUN pip install pathlib
RUN pip install celery
RUN pip install pillow
RUN pip install python-magic-bin==0.4.14

CMD [ "python", "./main.py" ]