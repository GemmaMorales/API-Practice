"""empty message

Revision ID: 3a705f479474
Revises: 84b9b897ba38
Create Date: 2020-04-30 14:11:28.449817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a705f479474'
down_revision = '84b9b897ba38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('done', table_name='todos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('done', 'todos', ['done'], unique=True)
    # ### end Alembic commands ###
