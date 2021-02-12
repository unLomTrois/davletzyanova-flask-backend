from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.db.models import Base, Note
import os

# init engine for connection
engine = create_engine(
    "postgres://ppywjtapzpplxn:dc56951a5ed768a6b999a7a78ad5daf74e37f011615e08a5146bdbbf1f88b907@ec2-52-205-3-3.compute-1.amazonaws.com:5432/dalqmdcogh770i",
    echo=True,
)

# init database
Base.metadata.create_all(engine)

# init session
Session = scoped_session(sessionmaker(bind=engine))
