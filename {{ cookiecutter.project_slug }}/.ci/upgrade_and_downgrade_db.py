#!/usr/bin/env python
import os

from alembic import command
from alembic.config import Config

{{ cookiecutter.project_slug.upper() }}_TEST_DB_URL = "{{ cookiecutter.project_slug.upper() }}_TEST_DB_URL"


def main():
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", "{{ cookiecutter.project_slug }}:migrations")
    alembic_cfg.set_main_option("sqlalchemy.url", os.environ[{{ cookiecutter.project_slug.upper() }}_TEST_DB_URL].strip())

    alembic_cfg.print_stdout("Upgrade to head:")
    command.upgrade(alembic_cfg, "head")
    command.history(alembic_cfg, indicate_current=True)

    alembic_cfg.print_stdout("\nDowngrade to base:")
    command.downgrade(alembic_cfg, "base")
    command.history(alembic_cfg, indicate_current=True)


if __name__ == "__main__":
    main()
