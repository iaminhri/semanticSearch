FROM python:3.12-bookworm

LABEL authors="iaminhridoy"

ENV PYTHONUNBUFFERED=1

WORKDIR /semanticSearch

COPY ./requirements.txt ./requirements.txt
COPY ./scripts /scripts

# RUN pip install -r /requirements.txt

COPY ./semanticSearch /semanticSearch

EXPOSE 8080

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get install -y --no-install-recommends git postgresql-client build-essential postgresql-client libpq-dev && \
    /py/bin/pip install -r /semanticSearch/requirements.txt && \
    apt-get remove -y build-essential libpq-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    # adduser --disabled-password --no-create-home ghost && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/media/audio && \
    mkdir -p /vol/web/media/images && \
    mkdir -p /vol/web/media/data && \
    mkdir -p /vol/web/media/embeddings && \
    mkdir -p /vol/web/media/media && \
    mkdir -p /vol/web/media/transcripts && \
    # chown -R ghost:ghost /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

# RUN adduser -D ghost
# RUN chown -R ghost:ghost /vol
# RUN chmod -R 755 /vol/web

COPY ./semanticSearch/media/media/* /vol/web/media/media/
COPY ./semanticSearch/media/images/* /vol/web/media/images/
COPY ./semanticSearch/media/data/* /vol/web/media/data/
COPY ./semanticSearch/media/transcripts/* /vol/web/media/transcripts/
COPY ./semanticSearch/media/embeddings/* /vol/web/media/embeddings/
COPY ./semanticSearch/static/* /vol/web/static/


ENV PATH="/scripts:/py/bin:$PATH"

# USER ghost

CMD ["run.sh"]
# CMD manage.py runserver 0.0.0.0:8000

