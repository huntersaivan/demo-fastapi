"""create posts table

Revision ID: 67b4f651d43f
Revises: 
Create Date: 2021-11-07 13:01:39.222530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67b4f651d43f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('title', sa.NVARCHAR(254), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
