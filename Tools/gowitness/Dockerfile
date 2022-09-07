FROM golang:1 as build

RUN apt-get update \
        && apt install git -y \
        && apt clean

WORKDIR /src

RUN git clone https://github.com/sensepost/gowitness
WORKDIR /src/gowitness

RUN make docker

FROM chromedp/headless-shell:latest

RUN export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
  dumb-init \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY --from=build /src/gowitness/gowitness /usr/local/bin

EXPOSE 7171

WORKDIR /qemuno

ENTRYPOINT ["gowitness"]
