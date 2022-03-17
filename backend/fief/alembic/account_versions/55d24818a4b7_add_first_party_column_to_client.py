"""Add first-party column to Client

Revision ID: 55d24818a4b7
Revises: 6b10f4d6ecee
Create Date: 2022-03-07 08:31:01.642177

"""
import sqlalchemy as sa
from alembic import op

import fief

# revision identifiers, used by Alembic.
revision = "55d24818a4b7"
down_revision = "6b10f4d6ecee"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "fief_clients",
        sa.Column(
            "first_party", sa.Boolean(), nullable=False, server_default=sa.false()
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("fief_clients", "first_party")
    # ### end Alembic commands ###