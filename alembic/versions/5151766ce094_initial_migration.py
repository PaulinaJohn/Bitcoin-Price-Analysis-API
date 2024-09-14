"""Initial migration

Revision ID: 5151766ce094
Revises: 
Create Date: 2024-09-14 02:30:28.910807

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '5151766ce094'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bitcoin_prices', 'date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)
    op.alter_column('bitcoin_prices', 'adj_close',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('bitcoin_prices', 'volume',
               existing_type=sa.NUMERIC(),
               type_=sa.BigInteger(),  # Changed from Integer to BigInteger
               existing_nullable=False)
    op.drop_index('idx_bitcoin_prices_date', table_name='bitcoin_prices')
    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_bitcoin_prices_date', 'bitcoin_prices', ['date'], unique=False)
    op.alter_column('bitcoin_prices', 'volume',
                type_=sa.NUMERIC(),  # Revert to NUMERIC
                existing_type=sa.BigInteger(),
                existing_nullable=False)
    op.alter_column('bitcoin_prices', 'adj_close',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('bitcoin_prices', 'date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    # ### end Alembic commands ###