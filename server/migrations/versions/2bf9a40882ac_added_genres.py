"""added genres

Revision ID: 2bf9a40882ac
Revises: 93f890c6a745
Create Date: 2023-08-07 18:06:04.066059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bf9a40882ac'
down_revision = '93f890c6a745'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genre_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_song_genre', 'genres', ['genre_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.drop_constraint('fk_song_genre', type_='foreignkey')
        batch_op.drop_column('genre_id')

    # ### end Alembic commands ###