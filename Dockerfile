FROM python:3.9

WORKDIR /fastapi-app

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]
