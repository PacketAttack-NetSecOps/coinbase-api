FROM python:3.12.8


WORKDIR /app


COPY ./requirements /app


RUN pip install --no-cache-dir -r /app/requirements.txt 


CMD ["/bin/sh"]