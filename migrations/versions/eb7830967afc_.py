"""empty message

Revision ID: eb7830967afc
Revises: bff1743be65c
Create Date: 2019-03-13 15:35:32.721082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb7830967afc'
down_revision = 'bff1743be65c'
branch_labels = None
depends_on = None


def upgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_column('message', 'timestamp')
    #op.add_column('notification', sa.Column('time_stamp', sa.Float(), nullable=True))
    #op.create_index(op.f('ix_notification_time_stamp'), 'notification', ['time_stamp'], unique=False)
    #op.drop_index('ix_notification_timestamp', table_name='notification')
    #op.drop_column('notification', 'timestamp')
    #op.drop_column('post', 'timestamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    op.add_column('notification', sa.Column('timestamp', sa.FLOAT(), nullable=True))
    op.create_index('ix_notification_timestamp', 'notification', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_notification_time_stamp'), table_name='notification')
    op.drop_column('notification', 'time_stamp')
    op.add_column('message', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###