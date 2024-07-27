"""init

Revision ID: be39af84989f
Revises: dfcd6124da1b
Create Date: 2024-07-27 18:02:48.662296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be39af84989f'
down_revision: Union[str, None] = 'dfcd6124da1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(length=55),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.alter_column('posts', 'content',
               existing_type=sa.VARCHAR(length=55),
               type_=sa.String(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'content',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=55),
               existing_nullable=False)
    op.alter_column('posts', 'title',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=55),
               existing_nullable=False)
    # ### end Alembic commands ###