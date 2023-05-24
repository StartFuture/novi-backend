FROM python:3.10-alpine

WORKDIR /api_teste

COPY . /api_teste

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]