"""empty message

Revision ID: c722db72fcb2
Revises: 
Create Date: 2024-03-11 11:58:36.974726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c722db72fcb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column('answer',
               existing_type=sa.VARCHAR(length=5),
               nullable=True)
        batch_op.alter_column('is_correct',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column('is_correct',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('answer',
               existing_type=sa.VARCHAR(length=5),
               nullable=False)

    # ### end Alembic commands ###