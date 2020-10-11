FROM python:3.7.4-buster as ci

RUN apt-get update && apt-get install -y postgresql-client

ENV CI_POETRY_URL="https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py"
ENV PATH="/root/.poetry/bin:${PATH}"
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
#ENV  PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
ENV POETRY_VERSION={{ cookiecutter.poetry_version }}

RUN curl -sSL "$CI_POETRY_URL" | python

RUN poetry config virtualenvs.create false

WORKDIR /{{ cookiecutter.project_slug }}

COPY poetry.lock pyproject.toml ./

RUN poetry install -n --no-root && poetry show


FROM ci as install

COPY . .

RUN poetry install


FROM install as local

CMD ["echo", "add command for local development"]


FROM install as production

CMD ["echo", "add production command"]
