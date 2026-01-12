# ...new file...
FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# system deps for common Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git curl && \
    rm -rf /var/lib/apt/lists/*

# copy files and install python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r /app/requirements.txt

# download spaCy small model deterministically
RUN python -m spacy download en_core_web_sm

# copy source
COPY src/ /app/src/
COPY config.py /app/src/config.py

WORKDIR /app/src

# default command runs harness (override in development)
CMD ["python", "harness.py"]