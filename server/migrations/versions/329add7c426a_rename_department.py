"""rename department

Revision ID: 329add7c426a
Revises: 1cab0a93a845
Create Date: 2025-03-05 17:57:27.163954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '329add7c426a'
down_revision = '1cab0a93a845'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
