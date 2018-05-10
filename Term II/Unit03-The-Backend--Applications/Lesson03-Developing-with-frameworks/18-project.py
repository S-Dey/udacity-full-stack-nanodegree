from flask import Flask, jsonify, redirect, render_template, request, url_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Restaurant, MenuItem

# Creating instance of Flask
app = Flask(__name__)

# SQLAlchemy setup
engine = create_engine("sqlite:///restaurantmenu.db")
Session = sessionmaker(bind=engine)
session = Session()


# Show a menu item by its ID.
@app.route("/")
@app.route("/menu_items/<int:menuitem_id>/")
def menu_items(menuitem_id):
    results = session.query(MenuItem).filter_by(id=menuitem_id).all()
    return render_template("menu.html", results=results)


# Edit a menu item by its ID
@app.route("/menu_items/<int:menuitem_id>/edit/", methods=['GET', 'POST'])
def edit_menu_item(menuitem_id):
    item_to_edit = session.query(MenuItem).filter_by(id=menuitem_id).one()

    if request.method == "POST":
        if request.form["name"]:
            item_to_edit.name = request.form["name"]
        session.add(item_to_edit)
        session.commit()
        return redirect(url_for("menu_items", menuitem_id=menuitem_id))
    else:
        return render_template("edit.html", menuitem_id=menuitem_id,
                               item_to_edit=item_to_edit)


# Create a new menu item referenced by a particular restaurant.
@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('menu_items', menuitem_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


# Delete a menu item.
@app.route("/menu_items/<int:menuitem_id>/delete/")
def delete_menu_item(menuitem_id):
    item_to_delete = session.query(MenuItem).filter_by(id=menuitem_id).one()
    session.delete(item_to_delete)
    session.commit()
    return render_template("delete_message.html", item_deleted=item_to_delete)


# Show data in JSON format.
@app.route("/menu_items/<int:menuitem_id>/JSON/")
def show_json_data(menuitem_id):
    menuitem = session.query(MenuItem).filter_by(id=menuitem_id).one()
    return jsonify(id=menuitem.id,
                   name=menuitem.name,
                   description=menuitem.description,
                   price=menuitem.price,
                   course=menuitem.course)


@app.route('/restaurants/<int:restaurant_id>/menu/JSON/')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
