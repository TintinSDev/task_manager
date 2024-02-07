"""Edited users table

Revision ID: a687ff61a466
Revises: 80326bac8f9e
Create Date: 2024-02-07 20:41:38.025515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a687ff61a466'
down_revision: Union[str, None] = '80326bac8f9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
