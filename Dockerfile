FROM python:3.11-slim as builder

WORKDIR /app

RUN pip install --no-cache-dir uv && \
    uv venv -p python3.11 /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY pyproject.toml requirements.txt ./

RUN uv pip install --no-cache -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

COPY scripts/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

COPY . .

CMD ["python", "main.py"]
