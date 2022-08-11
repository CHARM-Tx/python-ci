FROM python:3 AS base

WORKDIR /app
COPY setup.cfg setup.py pyproject.toml ./
COPY .git ./.git

FROM base AS test

RUN --mount=type=ssh --mount=type=cache,target=/root/.cache/pip pip install --editable .[tests]
COPY . .

FROM base

RUN --mount=type=ssh --mount=type=cache,target=/root/.cache/pip pip install --editable .
COPY . .
