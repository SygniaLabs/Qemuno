FROM python:3.8-alpine as compile
WORKDIR /opt
RUN apk add --no-cache --virtual .build-deps build-base openssl bzip2 dbus glib git gcc musl-dev python3-dev \
        libffi-dev libxslt libxslt-dev libgcrypt-dev libxml2 libxml2-dev openssl-dev dbus-libs dbus-dev dbus-glib-dev \
        linux-headers rust cargo make 
RUN python3 -m pip install virtualenv
RUN virtualenv -p python venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install git+https://github.com/SecureAuthCorp/impacket 
RUN pip install git+https://github.com/fox-it/BloodHound.py 
RUN apk del .build-deps

FROM python:3.8-alpine
COPY --from=compile /opt/venv/ /opt/venv/
WORKDIR /qemuno
ENTRYPOINT /opt/venv/bin/bloodhound-python

