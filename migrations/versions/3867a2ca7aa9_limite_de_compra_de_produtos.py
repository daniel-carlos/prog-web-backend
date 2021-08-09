"""limite de compra de produtos

Revision ID: 3867a2ca7aa9
Revises: d3794c633cdc
Create Date: 2021-08-08 11:41:45.493140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3867a2ca7aa9'
down_revision = 'd3794c633cdc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('limit', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'limit')
    # ### end Alembic commands ###