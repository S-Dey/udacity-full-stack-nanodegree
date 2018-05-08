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

"""
count = 0

for menu_item in menu_items:
    count += 1

print(count)
"""

"""
for menu_item in menu_items:
    print("ID: ", menu_item.id)
    print("Name: ", menu_item.name)
    print("Description: ", menu_item.description)
    print("Price: ", menu_item.price)
    print("Course: ", menu_item.course)
    print("Restaurant_ID: ", menu_item.restaurant_id)
    print("Restaurant: ", menu_item.restaurant)
    print("\n\n")
"""


one_item = session.query(MenuItem).filter_by(id=3).one()
print(type(one_item))
print(type(one_item.name))
print(one_item.name)
