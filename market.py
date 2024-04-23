from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
db=SQLAlchemy(app)


class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False,unique=True)
    price=db.Column(db.Integer(),nullable=False)
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)
    description=db.Column(db.String(length=1024),nullable=False,unique=True)

    def __repr__(self):
        return f'Item {self.name}'


@app.route("/")      #decorator
@app.route('/home')
def home_page():
    return render_template('home.html')


#Dynamic Routes
@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is a about page for {username}</h1>'

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items=items)







# from market import Item,db,app
# app.app_context().push()