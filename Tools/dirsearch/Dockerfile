FROM python:3.8-alpine as compile
WORKDIR /opt
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev
RUN python3 -m pip install virtualenv
RUN virtualenv -p python venv
ENV PATH="/opt/venv/bin:$PATH"
RUN python3 -m pip install dirsearch

FROM python:3.8-alpine
COPY --from=compile /opt/venv /opt/venv
WORKDIR /qemuno
ENTRYPOINT ["/opt/venv/bin/dirsearch"]
