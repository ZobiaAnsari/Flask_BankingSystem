"""add column to user

Revision ID: 206083c27dc2
Revises: f6f6a4692b06
Create Date: 2024-06-05 12:01:53.939820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '206083c27dc2'
down_revision: Union[str, None] = 'f6f6a4692b06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user', sa.Column('balance', sa.Integer(), default=0.0))


def downgrade() -> None:
    pass
