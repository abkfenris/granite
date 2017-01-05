"""Added Parking and Path

Revision ID: 0409c7092d1a
Revises: cabe73ebc292
Create Date: 2017-01-02 23:09:47.210295

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = '0409c7092d1a'
down_revision = 'cabe73ebc292'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=4326), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paths',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='MULTILINESTRING', srid=4326), nullable=True),
    sa.Column('public', sa.Boolean(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('projects', sa.Column('public', sa.Boolean(), nullable=True))
    #op.drop_index('idx_projects_geom', table_name='projects')
    op.add_column('slopes', sa.Column('public', sa.Boolean(), nullable=True))
    #op.drop_index('idx_slopes_geom', table_name='slopes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.create_index('idx_slopes_geom', 'slopes', ['geom'], unique=False)
    op.drop_column('slopes', 'public')
    #op.create_index('idx_projects_geom', 'projects', ['geom'], unique=False)
    op.drop_column('projects', 'public')
    op.drop_table('paths')
    op.drop_table('parking')
    # ### end Alembic commands ###