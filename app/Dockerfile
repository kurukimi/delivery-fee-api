FROM python:3.10

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src
COPY ./test ./test

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]