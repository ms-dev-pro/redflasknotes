FROM python:3.6-alpine
ADD . /core
WORKDIR /core
RUN pip install -r requirements.txt
CMD ["python", "app.py"]