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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
