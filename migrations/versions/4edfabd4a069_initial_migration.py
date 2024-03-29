"""Initial Migration

Revision ID: 4edfabd4a069
Revises: 216e88587a41
Create Date: 2022-05-08 19:19:07.101450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4edfabd4a069'
down_revision = '216e88587a41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
