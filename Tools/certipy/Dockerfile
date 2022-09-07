FROM python:3.8-alpine as compile
WORKDIR /opt
RUN apk add --no-cache git gcc musl-dev python3-dev openssl-dev libffi-dev 
RUN python3 -m pip install virtualenv
RUN virtualenv -p python venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install git+https://github.com/ly4k/Certipy

FROM python:3.8-alpine
COPY --from=compile /opt/venv /opt/venv
WORKDIR /qemuno
ENTRYPOINT ["/opt/venv/bin/certipy"]
