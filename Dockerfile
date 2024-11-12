FROM python:3.12.3-slim AS builder

COPY poetry.lock pyproject.toml ./

RUN python -m pip install poetry>=1.8.4 && \
    poetry export -o requirements.prod.txt --without-hashes && \
    poetry export --with=dev -o requirements.dev.txt --without-hashes

FROM python:3.12.3-slim AS dev

WORKDIR /app
COPY --from=builder requirements.dev.txt /app

RUN apt update -y && apt install --no-install-recommends -y \
    python3-dev && \
    pip install --upgrade pip --no-cache-dir --user -r requirements.dev.txt && \
    apt clean && rm -rf /var/lib/apt/lists/* requirements.dev.txt

FROM python:3.12.3-slim AS dev-runtime


