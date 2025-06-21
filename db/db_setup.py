from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE_URL

# Base class for the models
Base = declarative_base()

# Create the SQLite engine
# engine = create_engine(DATABASE_URL)
engine = create_engine(
    DATABASE_URL,
    pool_size=50,
    max_overflow=50,
    pool_timeout=60,
    pool_recycle=600  # Recycle connections after 10 mins to prevent stale connections
)

# Create a session factory
Session = sessionmaker(bind=engine)

# Initialize the session
def get_session():
    return Session()

# Initialize database (create tables)
def init_db():
    from db.models import General  # Import models
    Base.metadata.create_all(engine)
