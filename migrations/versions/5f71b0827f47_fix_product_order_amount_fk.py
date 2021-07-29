"""fix product_order amount FK

Revision ID: 5f71b0827f47
Revises: d1b970c9b7bd
Create Date: 2021-07-22 10:14:50.109903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f71b0827f47'
down_revision = 'd1b970c9b7bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product_order', 'amount',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('product_order_amount_fkey', 'product_order', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('product_order_amount_fkey', 'product_order', 'order', ['amount'], ['id'])
    op.alter_column('product_order', 'amount',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###