# Qualabinance backtest-engine worker.
# Lightweight image: only the deps needed to run projects/04-backtest-engine and
# import daytrad's real strategy functions through the CEO-approved read-only
# adapter. Research code + daytrad are bind-mounted at runtime (see compose), so
# this image only provides the Python environment.
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-backtest.txt .
RUN pip install --no-cache-dir -r requirements-backtest.txt

# Idle research worker: run backtests on demand via
#   docker exec -w /app/qualabinance/projects/04-backtest-engine \
#     qualabinance_backtest python3 validate_squad.py
CMD ["sleep", "infinity"]