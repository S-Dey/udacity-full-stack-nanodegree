from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

from pprint import pprint


engine = create_engine('sqlite:///restaurantmenu.db')

Session = sessionmaker(bind=engine)
session = Session()

menu_items = session.query(MenuItem).all()

"""
for menu_item in menu_items:
    pprint(vars(menu_item))
    print("\n")

for menu_item in menu_items:
    print(menu_item.name)
"""

count = 0

for menu_item in menu_items:
    count += 1

print(count)
