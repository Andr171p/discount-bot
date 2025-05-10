"""username may contains null

Revision ID: d8dfaf70fb4c
Revises: 8a682e923a68
Create Date: 2024-12-07 15:15:32.061039

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8dfaf70fb4c'
down_revision: Union[str, None] = '8a682e923a68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
