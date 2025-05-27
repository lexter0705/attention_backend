FROM python:3.12.8

COPY requirements.txt .

RUN pip install -r ./requirements.txt

COPY . .

CMD ["uvicorn", "run", "main:app", "--port", "80", "--host", "127.0.0.1"]