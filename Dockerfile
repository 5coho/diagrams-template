FROM python:3.12-slim-bullseye

RUN apt-get update && apt-get install -y gcc graphviz

WORKDIR /app

COPY . .

RUN pip install -r src/requirements.txt

CMD ["python", "src/main.py"]
