FROM python:3.8-alpine as compile
WORKDIR /opt
RUN apk add --no-cache git gcc musl-dev python3-dev openssl-dev libffi-dev libxslt-dev autoconf g++ python3-dev krb5-dev libxml2-dev
RUN python3 -m pip install virtualenv
RUN virtualenv -p python venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install git+https://github.com/byt3bl33d3r/CrackMapExec

FROM python:3.8-alpine
COPY --from=compile /opt/venv /opt/venv
RUN apk add --no-cache openssl openssl-dev binutils
WORKDIR /qemuno
RUN /opt/venv/bin/crackmapexec --help
ENTRYPOINT ["/opt/venv/bin/crackmapexec"]
