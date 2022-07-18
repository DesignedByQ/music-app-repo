from application import db
  
class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    feature = db.Column(db.String(30), default="None", nullable=False)
    category = db.Column(db.String(30), nullable=False)
    reldate = db.Column('Date', db.String(30), nullable=False)
    length = db.Column(db.Float, nullable=False)
    