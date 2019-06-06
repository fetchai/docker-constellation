FROM alpine:3.9 as builder

RUN mkdir -p /build /src

RUN apk add \
        bash \
        cmake \
        make \
        musl-dev \
        openssl-dev \
        python3-dev \
        gcc \
        git \
        g++ \
        clang-dev \
        libexecinfo-dev \
        linux-headers

ENV CC=clang
ENV CXX=clang++

WORKDIR /build

ARG ledger_tag=v0.3.1-rc1

RUN git clone https://github.com/fetchai/ledger.git -b ${ledger_tag} --quiet /src
RUN cd /src && git submodule --quiet update --init --recursive

RUN cmake /src && make -j8 constellation

FROM alpine:3.9

RUN mkdir -p /app/data && \
    apk add \
        openssl \
        libstdc++

WORKDIR /app/data

COPY --from=builder /build/apps/constellation/constellation /app/constellation

VOLUME [ "/app/data" ]

EXPOSE 8000 8001 8010 8011

ENTRYPOINT [ "/app/constellation" ]
CMD ["-standalone", "-block-interval", "3000"]
