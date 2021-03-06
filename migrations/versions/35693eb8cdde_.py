"""empty message

Revision ID: 35693eb8cdde
Revises: d1e8bb87d422
Create Date: 2019-11-21 10:36:33.472111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35693eb8cdde'
down_revision = 'd1e8bb87d422'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cluster', sa.Column('ui_parameters', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cluster', 'ui_parameters')
    # ### end Alembic commands ###
