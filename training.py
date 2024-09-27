from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
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
    nome = db.Column(db.String(50))
    preco = db.Column(db.Float)
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def to_json(self):
        return {"id": self.id, "nome": self.nome, "preco": float(self.preco)}
    
with app.app_context():
    db.create_all()
    
@app.route("/persons", methods=["GET"])
def select_users():
    person_objects = Person.query.all()
    persons_json = [persons.to_json() for persons in person_objects]
    
    return generate_response(200, "persons", persons_json, "ok")

@app.route("/persons/<id>", methods=["GET"])
def select_user(id):
    person_object = Person.query.filter_by(id=id).first()
    person_json = person_object.to_json()
    
    return generate_response(200, "persons", person_json)

@app.route("/add", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        try:
            newPerson = Person(request.form['nome'], request.form['preco'])
            db.session.add(newPerson)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
            return generate_response(400, "person", {}, "Error to created")
    return render_template('add.html')
    
@app.route("/edit/<id>", methods=["GET", 'POST'])
def update(id):
    person = Person.query.get(id)
    if request.method == "POST":
        # pegar os dados que vinheram da requisição
        try:
            person.nome = request.form['nome']
            person.preco = request.form['preco']
            db.session.add(person)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
            return generate_response(400, "person", {}, "Error to update")
    return render_template('edit.html', person=person)
    
@app.route("/delete/<id>")
def delete(id):
    person_object = Person.query.get(id)
    try:
        db.session.delete(person_object)
        db.session.commit()
        return redirect(url_for('index'))
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

@app.route("/persons/<user_nome>")
def users(user_nome):
    return render_template("users.html", user_nome=user_nome)

def generate_response(status, content_nome, content, msg=False):
    body = {}
    body[content_nome] = content
    
    if(msg):
        body["message"] = msg
        
    return Response(json.dumps(body), status=status, mimetype="application/json")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)