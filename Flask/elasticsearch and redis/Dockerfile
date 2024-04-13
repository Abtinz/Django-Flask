FROM python:3.9.19-alpine

#requirements that we need will copied here for pip install process
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#flask port
EXPOSE 5000

CMD ["python", "./main.py"]