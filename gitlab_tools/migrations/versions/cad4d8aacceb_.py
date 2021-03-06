"""empty message

Revision ID: cad4d8aacceb
Revises: 6ea24c49b7a1
Create Date: 2018-06-08 01:36:29.014684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cad4d8aacceb'
down_revision = '6ea24c49b7a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pull_mirror', sa.Column('periodic_task_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_pull_mirror_periodic_task_id'), 'pull_mirror', ['periodic_task_id'], unique=False)
    op.create_foreign_key(None, 'pull_mirror', 'periodic_task', ['periodic_task_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pull_mirror', type_='foreignkey')
    op.drop_index(op.f('ix_pull_mirror_periodic_task_id'), table_name='pull_mirror')
    op.drop_column('pull_mirror', 'periodic_task_id')
    # ### end Alembic commands ###
