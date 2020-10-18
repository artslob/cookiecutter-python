#!/usr/bin/env python

import argparse
import os

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, drop_database

from {{ cookiecutter.project_slug }}.orm import metadata

{{ cookiecutter.project_slug.upper() }}_TEST_DB_URL = "{{ cookiecutter.project_slug.upper() }}_TEST_DB_URL"


def parse_args():
    parser = argparse.ArgumentParser(description="Upgrade database.")
    parser.add_argument("--method", choices=["meta", "migration"], required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    db_url = os.environ[{{ cookiecutter.project_slug.upper() }}_TEST_DB_URL].strip()
    drop_database(db_url)
    create_database(db_url)
    engine = create_engine(db_url)

    if args.method == "meta":
        metadata.create_all(engine)
        return

    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", "{{ cookiecutter.project_slug }}:migrations")
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)
    command.upgrade(alembic_cfg, "head")
    engine.execute("DROP TABLE IF EXISTS alembic_version CASCADE;")


if __name__ == "__main__":
    main()
    print("upgraded successfully")
