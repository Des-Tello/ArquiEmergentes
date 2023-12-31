FROM python:alpine3.18

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask python-dotenv

RUN apk add --no-cache sqlite

EXPOSE 5000

CMD ["python", "API.py"]