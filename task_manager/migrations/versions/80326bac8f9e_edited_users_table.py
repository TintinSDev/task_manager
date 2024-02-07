"""Edited users table

Revision ID: 80326bac8f9e
Revises: b3bba2009542
Create Date: 2024-02-07 20:36:10.140972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80326bac8f9e'
down_revision: Union[str, None] = 'b3bba2009542'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
