"""empty message

Revision ID: 4ae2d4c0d1af
Revises: 
Create Date: 2022-09-01 13:11:34.767732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae2d4c0d1af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loanapp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loan_type', sa.String(), nullable=True),
    sa.Column('loan_amount', sa.Integer(), nullable=True),
    sa.Column('property_type', sa.String(), nullable=True),
    sa.Column('property_address', sa.String(), nullable=True),
    sa.Column('under_contract', sa.String(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('llc_name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('referral', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('user_loan',
    sa.Column('loan_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['loan_id'], ['loanapp.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_loan')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('loanapp')
    # ### end Alembic commands ###
