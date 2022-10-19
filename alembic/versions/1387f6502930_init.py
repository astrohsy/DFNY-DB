# flake8: noqa
"""init

Revision ID: 1387f6502930
Revises: 
Create Date: 2022-10-18 21:49:33.742365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1387f6502930'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dnyf_groups',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('group_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('group_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dnyf_groups')
    # ### end Alembic commands ###