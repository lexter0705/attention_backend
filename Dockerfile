FROM python:3.12.8

COPY requirements.txt .

RUN pip install -r ./requirements.txt

COPY . .

CMD ["uvicorn", "run", "main:app", "-p", "80", "-h", "0.0.0.0"]