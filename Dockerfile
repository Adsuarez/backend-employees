FROM python:3

RUN mkdir -p /home/app

WORKDIR /home/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 1234

WORKDIR /home/app/crud

CMD ["python", "manage.py", "runserver"]