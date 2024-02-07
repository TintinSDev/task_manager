"""FUll

Revision ID: 71bf6d8ad7df
Revises: 86b25dc2c1ee
Create Date: 2024-02-06 23:41:45.168357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '71bf6d8ad7df'
down_revision: Union[str, None] = '86b25dc2c1ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create a new table with the desired changes
    op.create_table('users_new',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        # Add other columns here as needed
        ...
    )

    # Copy data from the old table to the new one
    op.execute('INSERT INTO users_new (id, username) SELECT id, username FROM users')

    # Drop the old table
    op.drop_table('users')


def downgrade():
    # Create a new table without the username column
    op.create_table('users_old',
        sa.Column('id', sa.Integer(), nullable=False),
        # Add other columns here as needed
        ...
    )

    # Copy data from the new table to the old one
    op.execute('INSERT INTO users_old (id) SELECT id FROM users_new')

    # Drop the new table
    op.drop_table('users_new')

