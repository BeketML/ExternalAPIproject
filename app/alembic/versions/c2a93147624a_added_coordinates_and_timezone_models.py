"""Added Coordinates and Timezone models

Revision ID: c2a93147624a
Revises: 3d2e880c8bb5
Create Date: 2024-12-05 18:10:14.525039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2a93147624a'
down_revision = '3d2e880c8bb5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_admins_id'), 'admins', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_admins_id'), table_name='admins')
    op.drop_table('admins')
    # ### end Alembic commands ###
