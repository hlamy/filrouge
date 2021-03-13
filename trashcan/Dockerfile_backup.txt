FROM python:3.7


ADD main.py /
ADD flaskroutes.py /
ADD settings.py /
ADD utilities.py /

RUN pip install flask
RUN pip install pathlib
RUN pip install celery
RUN pip install pillow
RUN pip install filemagic
RUN pip install filetype

CMD [ "python", "./main.py" ]