# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add_extra_column_to_columns_model

Revision ID: 181091c0ef16
Revises: 07071313dd52
Create Date: 2021-08-24 23:27:30.403308

"""

# revision identifiers, used by Alembic.
revision = "181091c0ef16"
down_revision = "021b81fe4fbb"

import sqlalchemy as sa  # noqa: E402
from alembic import op  # noqa: E402


def upgrade():
    with op.batch_alter_table("table_columns") as batch_op:
        batch_op.add_column(sa.Column("extra", sa.Text(), nullable=True))


def downgrade():
    with op.batch_alter_table("table_columns") as batch_op:
        batch_op.drop_column("extra")
