ARG SUPERSET_VERSION="3.1.1"
ARG PYTHON_VERSION="310"
ARG SUPERSET_BASE_IMAGE="apache/superset:$SUPERSET_VERSION-py$PYTHON_VERSION"

# Guide to extend Superset image https://hub.docker.com/r/apache/superset
FROM $SUPERSET_BASE_IMAGE AS gcc-builder

USER root

RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ python3-dev libgeos-dev git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

FROM gcc-builder AS python-builder
ARG SUPERSET_VERSION

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt apache-superset==$SUPERSET_VERSION

USER superset
