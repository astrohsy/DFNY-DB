"""
Main API entrypoint
"""
# Third party imports
from fastapi import FastAPI


# Local application imports
from .routes import group
from .routes import health
from .db.base import engine, Base
from .sample_data import add_sample_data

# Create all DB schema from scratch on every startup
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Add sample data to DB
add_sample_data()

app = FastAPI()
app.include_router(group.router)
app.include_router(health.router)
