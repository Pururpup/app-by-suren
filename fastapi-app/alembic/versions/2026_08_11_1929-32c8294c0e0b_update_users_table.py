"""update users table

Revision ID: 32c8294c0e0b
Revises: 052b48922f86
Create Date: 2026-08-11 19:29:44.966208

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "32c8294c0e0b"
down_revision: Union[str, Sequence[str], None] = "052b48922f86"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(
        op.f("uq_users_foo_bar"), "users", ["foo", "bar"]
    )


def downgrade() -> None:
    op.drop_constraint(op.f("uq_users_foo_bar"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
