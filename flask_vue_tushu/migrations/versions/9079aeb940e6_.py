"""empty message

Revision ID: 9079aeb940e6
Revises: 3415e995f0c3
Create Date: 2024-04-10 18:30:56.206796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9079aeb940e6'
down_revision = '3415e995f0c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ddddd', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('ddddd')

    # ### end Alembic commands ###
