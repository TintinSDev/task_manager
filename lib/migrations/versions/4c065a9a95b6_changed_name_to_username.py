"""Changed name to username

Revision ID: 4c065a9a95b6
Revises: c6c1393c631d
Create Date: 2024-02-06 22:47:08.486866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c065a9a95b6'
down_revision: Union[str, None] = 'c6c1393c631d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_categories_description', table_name='categories')
    op.drop_index('ix_categories_name', table_name='categories')
    op.add_column('tasks', sa.Column('username', sa.String(), nullable=True))
    op.drop_index('ix_tasks_name', table_name='tasks')
    op.create_index(op.f('ix_tasks_username'), 'tasks', ['username'], unique=False)
    op.drop_column('tasks', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_index(op.f('ix_tasks_username'), table_name='tasks')
    op.create_index('ix_tasks_name', 'tasks', ['name'], unique=False)
    op.drop_column('tasks', 'username')
    op.create_index('ix_categories_name', 'categories', ['name'], unique=False)
    op.create_index('ix_categories_description', 'categories', ['description'], unique=False)
    # ### end Alembic commands ###