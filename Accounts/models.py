from extensions.database import db

class Cookie():
  id = ''
  slug = ''
  name = ''
  price = ''






class accounts(db.Model):
  User_id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
  password_id = db.Column(db.Integer, db.ForeignKey('password.id'), primary_key=True)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True,)
  uname = db.Column(db.String(128))
  email = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
  
class Login_input(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))

password = db.relationship('Password', backref='order', uselist=False, lazy=True)