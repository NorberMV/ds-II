import logging
from sqlalchemy import (
        create_engine, 
        text,
)
import time

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.DEBUG)


time.sleep(5)

engine = create_engine("postgresql+psycopg2://admin:admin@db:5432/DB")

try:
    conn = engine.connect()
except Exception as e:
    logger.debug(f"Connection failed, see the logs:\n{e!r}")

query=text(
        "INSERT INTO sql_practice (_name, surname) VALUES ('Norber', 'MV'), ('Dey', 'Pequitas!');"
        )
try:
    logger.debug(f"Executing query: {query!r}")
    conn.execute(query)
except Exception as e:
    logger.debug(f"Query execution failed, find the logs: {e!r}")
else:
    conn.commit()
    logger.debug('Everything wen smoothly!!')
