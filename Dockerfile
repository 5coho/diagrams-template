FROM python:3.12-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y gcc graphviz

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
