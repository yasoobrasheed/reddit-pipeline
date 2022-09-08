"""create submissions table

Revision ID: c1adbd51dad3
Revises: 
Create Date: 2022-09-07 23:08:29.777425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c1adbd51dad3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "submissions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("subreddit", sa.String, nullable=False),
        sa.Column("title", sa.Unicode, nullable=False),
        sa.Column("author", sa.String, nullable=False),
        sa.Column("url", sa.String, nullable=False),
        sa.Column("submission_id", sa.String, nullable=False),
        sa.Column("submission_created_at", sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table("account")
