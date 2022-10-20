FROM python:3

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT ["python", "./cards_checker.py"]