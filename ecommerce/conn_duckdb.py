from functools import lru_cache
from pathlib import Path

import duckdb

db_path = Path.cwd() / 'data/database/ecommerce.db'


@lru_cache(maxsize=1)
def get_conn():
    return duckdb.connect(database=db_path)


def drop_db():
    if db_path.exists():
        db_path.unlink()
