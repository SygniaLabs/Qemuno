FROM python:3.9-alpine
WORKDIR /qemuno-ui
COPY . .
RUN apk add docker
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=run.py
ENTRYPOINT flask run --host=0.0.0.0 --port=5000