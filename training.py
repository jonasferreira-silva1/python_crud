from flask import Flask, render_template, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/training'
app.app_context()

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    
    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email}
    
with app.app_context():
    db.create_all()
    
@app.route("/users", methods=["GET"])
def select_users():
    person_objects = Person.query.all()
    persons_json = [persons.to_json() for persons in person_objects]
    
    return generate_response(200, "persons", persons_json, "ok")

@app.route("/users/<id>", methods=["GET"])
def select_user(id):
    person_object = Person.query.filter_by(id=id).first()
    person_json = person_object.to_json()
    
    return generate_response(200, "persons", person_json)

@app.route("/users", methods=["POST"])
def create():
    body = request.get_json()
    # Validar se os parametros irão vim corretamente (com try catch ou etc)
    try:
        person = Person(name=body["name"], email=body["email"])
        db.session.add(person)
        db.session.commit()
        return generate_response(201, "person", person.to_json(), "Created")
    except Exception as e:
        print(e)
        return generate_response(400, "person", {}, "Error to created")
    
@app.route("/users/<id>", methods=["PUT"])
def update(id):
    person_object = Person.query.filter_by(id=id).first()
    body = request.get_json()
    try:
        if('name' in body): # se o cara so for alterar o nome
            person_object.name = body['name']
        if('email' in body): # se so for o email
            person_object.email = body['email']
            
        db.session.add(person_object)
        db.session.commit()
        return generate_response(200, "person", person_object.to_json(), "Updated")
    except Exception as e:
        print(e)
        return generate_response(400, "person", {}, "Error to update")
    
@app.route("/users/<id>", methods=["DELETE"])
def delete(id):
    person_object = Person.query.filter_by(id=id).first()
    
    try:
        db.session.delete(person_object)
        db.session.commit()
        return generate_response(200, "person", person_object.to_json(), "Deleted")
    except Exception as e:
        print(e)
        return generate_response(400, "person", {}, "Error to delete")
        
@app.route("/")
def index():
    person = Person.query.all()
    return render_template("homepage.html", persons=person)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/users/<user_name>")
def users(user_name):
    return render_template("users.html", user_name=user_name)

def generate_response(status, content_name, content, msg=False):
    body = {}
    body[content_name] = content
    
    if(msg):
        body["message"] = msg
        
    return Response(json.dumps(body), status=status, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)