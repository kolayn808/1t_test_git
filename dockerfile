FROM python:3.9-slim

WORKDIR /usr/src/app

COPY app.py a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 .

ENTRYPOINT ["python", "app.py"]
