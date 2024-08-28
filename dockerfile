FROM python:3.9-slim

#WORKDIR /usr/src/app
WORKDIR /home/kolayn/docker_python_app

COPY app.py 1.txt 2.txt 34.txt 44.txt 45.txt app.txt test.txt test.py docker.txt dockerfile .

ENTRYPOINT ["python", "app.py"]
