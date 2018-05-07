from flask import Flask
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
def homepage():
    return """<h1>Welcome!</h1>
              <p>Welcome to my restaurant!</p>
        """


@app.route("/menu_items")
def menu_items():
    results = session.query(MenuItem).all()
    output = ''
    newline = "<br>"

    for result in results:
        output += str(result.id) + ". "
        output += result.name + newline
        output += result.description + newline
        output += result.course + newline
        output += str(result.restaurant_id) + newline + newline

    return output


@app.route("/restaurant_items")
def restaurant_all():
    results = session.query(Restaurant).all()
    output = ''

    for result in results:
        output += str(result.id) + ". " + result.name + '<br>'

    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
