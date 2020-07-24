FROM python:3.8-alpine3.12

COPY setup.py README.md /deploy/
COPY ./gerador_primos /deploy/gerador_primos/

WORKDIR /deploy/
RUN apk add python3-dev \
    && apk add build-base \
    && pip3 install -e .

EXPOSE 3000

CMD ["gunicorn", "-b", "0.0.0.0:3000", "-w", "1", "-k", "uvicorn.workers.UvicornH11Worker", "-t", "174000", "gerador_primos:app"]
