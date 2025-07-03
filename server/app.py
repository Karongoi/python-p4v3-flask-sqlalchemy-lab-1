from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    quake = Earthquake.query.filter_by(id=id).first()
    if quake:
        return jsonify(quake.to_dict()), 200
    return jsonify({"message": f"Earthquake {id} not found."}), 404
@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_quakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    quake_list = [quake.to_dict() for quake in quakes]

    return jsonify({
        "count": len(quake_list),
        "quakes": quake_list
    }), 200
