
FROM python:3.12.2

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

