"""Empty Init

Revision ID: 86b25dc2c1ee
Revises: c58f48a62a98
Create Date: 2024-02-06 23:32:23.666367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86b25dc2c1ee'
down_revision: Union[str, None] = 'c58f48a62a98'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass