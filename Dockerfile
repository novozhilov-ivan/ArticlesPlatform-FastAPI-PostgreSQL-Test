ARG IMAGE=python:3.13.2-slim-bullseye

FROM $IMAGE AS builder

COPY poetry.lock pyproject.toml ./

RUN : \
    && python -m pip install poetry==2.0.1 \
    && poetry self add poetry-plugin-export \
    && poetry export \
      --output=requirements.prod.txt \
      --without-hashes \
    && poetry export \
      --with=dev \
      --output=requirements.dev.txt \
      --without-hashes

FROM $IMAGE AS dev

WORKDIR /app
COPY --from=builder requirements.dev.txt /app

RUN : \
    && apt update \
    && apt install -y --no-install-recommends \
      python3-dev \
    && pip install \
      --upgrade pip \
      --no-cache-dir \
      --user \
      -r requirements.dev.txt \
    && apt clean \
    && rm -rf \
      /var/lib/apt/lists/* \
      requirements.dev.txt

FROM $IMAGE AS dev-runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/root/.local/bin:$PATH

COPY --from=dev /root/.local /root/.local
COPY src/ /app/src
COPY tests/ /app/tests
COPY alembic.ini /app/alembic.ini
COPY pytest.ini /app/pytest.ini
