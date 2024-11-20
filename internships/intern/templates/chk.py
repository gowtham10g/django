from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app=flask(__name__) #init method

app.config[''] ='sqlite://'     #i haven"t any databses urls so that where i do blank here
app.config['']=False
db=SQLAlchemy(app)

class User(db.model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)

    def __repr__(self):
        return f"<User{self.name}>"
    
@app.route('/')
def home():
       return "Database Connection Successfully!"


@app.route('/add_user/<name>/<email>')
def add_user(name,email):
            try:
               new_user=User(name=name,email=email)
               db.session.add(new_user)
               db.session.commit()
               return jsonify(("message":"User added Successfully!"))
            except Exception as e:
             return jsonify({"error":str(e)})

@app.route('/get_users')
 def get_users():
 
   users=User.query.all()
   retrun jsonify([{"id":user.id,"name":user.name,"email":user.email}])


if__name__=='__main__':

 with app.app_context():
    db.create_all()

    app.run(debug=True)
           
