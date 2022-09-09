"""add time metadata columns to submissions table

Revision ID: b8061c2c4fe9
Revises: c1adbd51dad3
Create Date: 2022-09-08 20:00:50.025945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b8061c2c4fe9"
down_revision = "c1adbd51dad3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("submissions", sa.Column("created_at", sa.DateTime))
    op.add_column("submissions", sa.Column("updated_at", sa.DateTime))
    op.add_column("submissions", sa.Column("deleted_at", sa.DateTime))


def downgrade() -> None:
    pass
