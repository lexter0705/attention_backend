FROM python:3.12.8

COPY requirements.txt .

RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]