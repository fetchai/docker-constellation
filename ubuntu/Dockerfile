FROM ubuntu:18.04 as builder

RUN mkdir -p /build /src && \
    apt-get update && \
    apt-get install -y \
        build-essential \
        libssl-dev \
        cmake \
        python3-dev \
        clang \
        git

WORKDIR /build

ARG ledger_tag=v0.5.1

RUN git clone https://github.com/fetchai/ledger.git -b ${ledger_tag} --quiet /src
RUN cd /src && git submodule --quiet update --init --recursive

ENV CC=clang
ENV CXX=clang++

RUN cmake /src && make -j8 constellation

FROM ubuntu:18.04

RUN mkdir -p /app/data && \
    apt-get update && \
    apt-get install -y \
        libssl1.1

WORKDIR /app/data

COPY --from=builder /build/apps/constellation/constellation /app/constellation

VOLUME [ "/app/data" ]

EXPOSE 8000 8001 8010 8011

ENTRYPOINT [ "/app/constellation" ]
CMD ["-standalone", "-block-interval", "3000"]
