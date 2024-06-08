"""create user

Revision ID: bc06487d9a0d
Revises: 
Create Date: 2024-06-04 16:36:47.995883

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc06487d9a0d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=False),
    sa.Column('accountNo', sa.String(length=30), nullable=False),
    sa.Column('accountPin', sa.String(length=4), nullable=False),
    sa.Column('address', sa.String(length=60), nullable=False),
    sa.Column('pin', sa.String(length=6), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email','phone','name')
    )


def downgrade() -> None:
    pass
