from flask import Flask, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Restaurant, MenuItem

# Creating instance of Flask
app = Flask(__name__)

# SQLAlchemy setup
engine = create_engine("sqlite:///restaurantmenu.db")
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/")
@app.route("/menu_items/<int:menuitem_id>/")
def menu_items(menuitem_id):
    results = session.query(MenuItem).filter_by(id=menuitem_id).all()
    return render_template("menu.html", results=results)


@app.route("/menu_items/<int:menuitem_id>/edit/")
def edit_menu_item(menuitem_id):
    results = session.query(MenuItem).filter_by(id=menuitem_id).all()
    return render_template("edit.html", menuitem_id=menuitem_id,
                           results=results)


@app.route("/menu_items/<int:menuitem_id>/delete/")
def delete_menu_item(menuitem_id):
    return "Delete Menu Item"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
