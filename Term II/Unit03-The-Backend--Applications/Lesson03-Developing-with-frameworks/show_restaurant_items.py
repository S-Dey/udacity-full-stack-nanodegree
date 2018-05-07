from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')

Session = sessionmaker(bind=engine)
session = Session()

restaurants = session.query(Restaurant).all()

for restaurant in restaurants:
    print(restaurant.id)
    print(restaurant.name)
    print("\n\n")
