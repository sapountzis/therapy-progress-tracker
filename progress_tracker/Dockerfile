FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.5.9 /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache --no-dev

COPY . .

CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]