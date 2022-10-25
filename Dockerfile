FROM python:3

WORKDIR /usr/src/app

COPY cards_checker.py .

ENTRYPOINT ["python", "./cards_checker.py"]