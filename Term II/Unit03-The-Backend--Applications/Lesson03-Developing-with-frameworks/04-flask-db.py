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


@app.route("/all_restaurants")
def hello():
    results = session.query(MenuItem).all()
    output = ''

    for result in results:
        output += result.name + '<br>'
    
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
