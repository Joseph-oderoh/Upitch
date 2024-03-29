"""Initial Migration

Revision ID: 6a4b4039dfcb
Revises: fa83c594ed71
Create Date: 2022-05-08 11:19:27.355242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a4b4039dfcb'
down_revision = 'fa83c594ed71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_emalil_key', 'users', type_='unique')
    op.drop_column('users', 'emalil')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('emalil', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_emalil_key', 'users', ['emalil'])
    # ### end Alembic commands ###
