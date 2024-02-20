"""empty message

Revision ID: f08c82925b99
Revises: 1194647d9d24
Create Date: 2024-02-21 00:11:51.842853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f08c82925b99'
down_revision: Union[str, None] = '1194647d9d24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
