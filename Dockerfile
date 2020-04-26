FROM python:3.7-slim
WORKDIR /test_task
COPY requirements.txt /test_task/
RUN pip install -r requirements.txt
COPY . /test_task/