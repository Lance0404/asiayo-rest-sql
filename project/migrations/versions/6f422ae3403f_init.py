"""init

Revision ID: 6f422ae3403f
Revises: 
Create Date: 2021-10-13 08:39:59.168778

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '6f422ae3403f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_create_at'), 'orders', ['create_at'], unique=False)
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=False)
    op.create_index(op.f('ix_orders_price'), 'orders', ['price'], unique=False)
    op.create_index(op.f('ix_orders_room_id'), 'orders', ['room_id'], unique=False)
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_property_id'), 'property', ['id'], unique=False)
    op.create_index(op.f('ix_property_name'), 'property', ['name'], unique=False)
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('property_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_room_id'), 'room', ['id'], unique=False)
    op.create_index(op.f('ix_room_name'), 'room', ['name'], unique=False)
    op.create_index(op.f('ix_room_property_id'), 'room', ['property_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_room_property_id'), table_name='room')
    op.drop_index(op.f('ix_room_name'), table_name='room')
    op.drop_index(op.f('ix_room_id'), table_name='room')
    op.drop_table('room')
    op.drop_index(op.f('ix_property_name'), table_name='property')
    op.drop_index(op.f('ix_property_id'), table_name='property')
    op.drop_table('property')
    op.drop_index(op.f('ix_orders_room_id'), table_name='orders')
    op.drop_index(op.f('ix_orders_price'), table_name='orders')
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.drop_index(op.f('ix_orders_create_at'), table_name='orders')
    op.drop_table('orders')
    # ### end Alembic commands ###