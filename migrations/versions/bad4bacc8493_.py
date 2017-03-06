"""empty message

Revision ID: bad4bacc8493
Revises: 8eaa98685eb3
Create Date: 2017-03-06 16:23:15.611360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bad4bacc8493'
down_revision = '8eaa98685eb3'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job_result', sa.Column('title', sa.String(length=200), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job_result', 'title')
    ### end Alembic commands ###
