"""init

Revision ID: a33a41c5e139
Revises: 
Create Date: 2021-10-13 09:52:44.932995

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'a33a41c5e139'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_property_id'), 'property', ['id'], unique=False)
    op.create_index(op.f('ix_property_name'), 'property', ['name'], unique=False)
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('property_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['property_id'], ['property.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_room_id'), 'room', ['id'], unique=False)
    op.create_index(op.f('ix_room_name'), 'room', ['name'], unique=False)
    op.create_index(op.f('ix_room_property_id'), 'room', ['property_id'], unique=False)
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_create_at'), 'order', ['create_at'], unique=False)
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    op.create_index(op.f('ix_order_price'), 'order', ['price'], unique=False)
    op.create_index(op.f('ix_order_room_id'), 'order', ['room_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_room_id'), table_name='order')
    op.drop_index(op.f('ix_order_price'), table_name='order')
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_index(op.f('ix_order_create_at'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_room_property_id'), table_name='room')
    op.drop_index(op.f('ix_room_name'), table_name='room')
    op.drop_index(op.f('ix_room_id'), table_name='room')
    op.drop_table('room')
    op.drop_index(op.f('ix_property_name'), table_name='property')
    op.drop_index(op.f('ix_property_id'), table_name='property')
    op.drop_table('property')
    # ### end Alembic commands ###