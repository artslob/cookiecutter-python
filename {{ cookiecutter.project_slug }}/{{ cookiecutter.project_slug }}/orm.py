from uuid import uuid4

import sqlalchemy
from sqlalchemy import TIMESTAMP, Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import expression

naming_convention = {
    "ix": "ix_%(column_0_N_label)s",
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = sqlalchemy.MetaData(naming_convention=naming_convention)

User = sqlalchemy.Table(
    "user",
    metadata,
    Column("uid", UUID(), default=uuid4, primary_key=True),
    Column("username", String(), nullable=False, unique=True),
    Column("disabled", Boolean(), nullable=False, default=False, server_default=expression.false()),
    Column("hashed_password", String(), nullable=False),
    Column("is_admin", Boolean(), server_default=expression.false(), nullable=False),
    Column("created", TIMESTAMP(timezone=True), nullable=False, index=True),
)
