FROM alpine:latest

RUN apk add --no-cache nmap nmap-scripts 

WORKDIR /qemuno
ENTRYPOINT ["/usr/bin/nmap"]
