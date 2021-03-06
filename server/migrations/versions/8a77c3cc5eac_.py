"""empty message

Revision ID: 8a77c3cc5eac
Revises: e160191ff485
Create Date: 2019-11-16 19:23:14.285537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a77c3cc5eac'
down_revision = 'e160191ff485'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('description', sa.String(), nullable=True))
    op.add_column('tasks', sa.Column('initiator_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'initiator_id')
    op.drop_column('tasks', 'description')
    # ### end Alembic commands ###
