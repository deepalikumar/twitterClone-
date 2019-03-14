"""empty message

Revision ID: 17f31a66408b
Revises: ecc74b94083e
Create Date: 2019-03-13 14:02:43.107491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17f31a66408b'
down_revision = 'ecc74b94083e'
branch_labels = None
depends_on = None


def upgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    #op.create_index(op.f('ix_post_time_stamp'), 'post', ['time_stamp'], unique=False)
   # op.drop_index('ix_post_timestamp', table_name='post')
   # op.drop_column('post', 'timestamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    op.create_index('ix_post_timestamp', 'post', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_post_time_stamp'), table_name='post')
    # ### end Alembic commands ###