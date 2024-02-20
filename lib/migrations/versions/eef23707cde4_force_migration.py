"""force migration

Revision ID: eef23707cde4
Revises: c6c1393c631d
Create Date: 2024-02-13 21:59:33.902005

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eef23707cde4'
down_revision: Union[str, None] = 'c6c1393c631d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
