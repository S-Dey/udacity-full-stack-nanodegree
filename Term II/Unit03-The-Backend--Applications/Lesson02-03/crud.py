from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Tell which database to communicate with.
engine = create_engine('sqllite://restaurantmenu.db')

# Makes connection between our class definitions and their corresponding
# tables within our database.
Base.metadata.bind = engine

# Establish a link of communication between our code executions and
# the engine we just created.
Session = sessionmaker(bind=engine)
session = Session()
