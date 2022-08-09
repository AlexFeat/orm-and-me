"""initialize 
Revision ID: 957232a5b7ee
Revises: 
Create Date: 2022-06-04 13:02:45.839649
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '957232a5b7ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE SCHEMA "happy_hog"')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stuff',
    sa.Column('id', postgresql.UUID(as_uuid=True), autoincrement=True, nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name'),
    schema='happy_hog'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stuff', schema='happy_hog')
    # ### end Alembic commands ###
    op.execute('DROP SCHEMA "happy_hog"')
