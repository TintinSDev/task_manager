"""Edited users table

Revision ID: b3bba2009542
Revises: 71bf6d8ad7df
Create Date: 2024-02-07 20:30:41.649013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3bba2009542'
down_revision: Union[str, None] = '71bf6d8ad7df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
