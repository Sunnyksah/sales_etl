from sqlalchemy import create_engine
from logger import logger
from config import DB_CONFIG

def get_db_engine():
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
            f"postgresql+psycopg2://{DB_CONFIG['port']}:{DB_CONFIG['database']}"
        )
        logger.info("PostgreSQL engine created successfully")
        return engine
    except Exception as e:
        logger.error(f"Failed to create DB engine: {e}")
        return None