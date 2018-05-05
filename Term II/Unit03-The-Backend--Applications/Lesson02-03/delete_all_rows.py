from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem
import sys


engine = create_engine('sqlite:///restaurantmenu.db')

Session = sessionmaker(bind=engine)
session = Session()

# Delete all rows
try:
    session.query(MenuItem).delete()
    session.commit()
    print("All rows deleted!")
except:
    sys.exit(1)
